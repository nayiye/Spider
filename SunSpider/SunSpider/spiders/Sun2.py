# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem

class Sun2Spider(scrapy.Spider):
    name = 'Sun2'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0

    def parse(self, response):
        ls = response.xpath('//div[@class="greyframe"]/table[2]//table//tr')
        print('len:',len(ls))
        for each in ls:
            item = SunspiderItem()
            item['number'] = each.xpath('./td[1]/text()').extract()[0]
            item['title'] = each.xpath('./td[2]/a[2]/text()').extract()[0]
            item['url'] = each.xpath('./td[2]/a[2]/@href').extract()[0]
            item['author'] = each.xpath('./td[4]/text()').extract()
            if len(item['author'])>0:
                item['author'] = item['author'][0]
            else:
                item['author'] = "空"
            item['pub_date'] = each.xpath('./td[5]/text()').extract()[0]
            req = scrapy.Request(item['url'],callback=self.parse_item)
            req.meta['item'] = item
            yield req

        # 翻页
        if self.offset <= 8000:
            self.offset += 30
            self.log('detail_url:'+self.url + str(self.offset))
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse,dont_filter=False)

    def parse_item(self,response):
        item = response.meta['item']
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]/text()').extract()
        item['content'] = ''.join(item['content'])
        yield item


