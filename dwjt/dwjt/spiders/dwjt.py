import scrapy

class DWJT(scrapy.Spider):
    name = 'dwjt'
    allowed_domains = ["daweijita.com"]
    start_urls = [
        "http://www.daweijita.com/2441.html"
    ]

    def parse(self, response):
        for item in response.xpath('//tr/td'):
            title = item.xpath('a/text()')
            print(title)