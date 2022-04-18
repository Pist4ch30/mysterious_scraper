import scrapy, json, requests, re
from scrapy_selenium import SeleniumRequest
from scrapy import Request

class IfconfigSpider(scrapy.Spider):
    name = 'ifconfig'


    def start_requests(self):
        url = "http://api.scraperapi.com?api_key=61c3e8fc0a503c7f86f6663ee1b4ef6a&url=http://httpbin.org/ip"
        yield Request(url=url, callback=self.parse)


    def parse(self, response):
        print(response.body)
        api_key = "4153f9c7c11b4b4896447f225b6d55c7"
        xlink = LinkExtractor()
        for link in xlink.extract_links(response):
            print(link)

        #print(requests.get(f'https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip["origin"]}').text)