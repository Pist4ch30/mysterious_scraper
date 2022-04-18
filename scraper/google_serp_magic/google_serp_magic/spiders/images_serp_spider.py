
# Import des modules scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
from scraper_api import ScraperAPIClient
import json, os
from dotenv import load_dotenv

load_dotenv()
client = ScraperAPIClient(os.getenv("API_KEY_SCRAPER"))

class GoogleImagesSpider(Spider):
    name = "google_images"

    start_queries = ['Rachat de credit sofinco', 'Rachat de pret sofinco']

    def start_requests(self):
            for keyword in self.start_queries:
                google_dict = {'tbm': 'isch', 'hl': 'fr', 'gl': 'fr', 'q': keyword.replace(" ", "+")}
                url = f'https://www.google.com/search?' + urlencode(google_dict)
                yield Request(client.scrapyGet(url=url), callback=self.parse)

    def parse(self, response):
        di = response.xpath('//div[*]/div/a/div/img').getall()
        print(di)