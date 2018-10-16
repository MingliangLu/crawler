import scrapy
from dwjt.items import DwjtItem
import time

class DWJT(scrapy.Spider):
    name = 'dwjt'
    allowed_domains = ["daweijita.com"]
    start_urls = [
        "http://www.daweijita.com/2441.html"
    ]
    def __init__(self):
        pass

    def parse(self, response):
        for item in response.xpath('//tr/td'):
            out_item = DwjtItem()
            title = item.xpath('a/text()').extract()
            if len(title) == 0:
                address = item.xpath('span/strong/a/@href').extract()                                
                title = item.xpath('span/strong/a/text()').extract()
                if len(title) == 0:
                    address = item.xpath('strong/span/a/@href').extract()
                    title = item.xpath('strong/span/a/text()').extract()

            else:
                address = item.xpath('a/@href').extract()
            if len(title) > 0 and len(address) > 0:
                # out_item['address'] = address
                # out_item['title'] = title
                # print(address)
                detail_url = response.urljoin(response.url,address)
                yield scrapy.Request(detail_url, callback=self.parse_addr_contents)
                time.sleep(5)            
            #print(len(out_item) )

    def parse_addr_contents(self,response):
        youku_url = response.xpath('.//div[@class="control-icon control-icon-youkulogs"]/a/@href').extract()
        print(response)
        print(youku_url)
        pass