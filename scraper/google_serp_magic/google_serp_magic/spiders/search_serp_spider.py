
# Import des modules scrapy
from scrapy import Spider, Request
from ..items import SearchItem
from urllib.parse import urlencode
from scraper_api import ScraperAPIClient
import json, os
from dotenv import load_dotenv

load_dotenv()
client = ScraperAPIClient(os.getenv("API_KEY_SCRAPER"))

class GoogleSearchSpider(Spider):
    name = "google_search"

    start_queries = ['Rachat de credit sofinco', 'Rachat de pret sofinco']

    def start_requests(self):
            for keyword in self.start_queries:
                google_dict = {'num': 100, 'hl':'fr', 'gl':'fr', 'q': keyword.replace(" ", "+")}
                url    = f'https://www.google.com/search?' + urlencode(google_dict)
                yield Request(client.scrapyGet(url=url), callback=self.parse)

    def parse(self, response):
        links = response.xpath('//div[*]/div[2]/div/div/div/div/div/div/div/a/@href').getall()
        titles = response.xpath('//div[*]/div/div/div/div/div/div/a/h3').getall()
        related_queries = response.xpath('//div[*]/div/a/div/b').getall()
        # Save Item => Search
        item = SearchItem()
        item['url'] = links
        item['title'] = titles
        item['related_searchs'] = related_queries
        yield item