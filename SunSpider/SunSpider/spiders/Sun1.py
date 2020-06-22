# -*- coding: utf-8 -*-
import scrapy
from SunSpider.items import SunspiderItem

class Sun1Spider(scrapy.Spider):
    '''解析投诉列表的页面'''
    name = 'Sun1'
    allowed_domains = ['wz.sun0769.com']
    # 入口地址
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    def parse(self, response):
        # 提取帖子链接的列表
        links = response.xpath('//a[@class="news14"]/@href').extract()
        print('len:',len(links))
        for link in links:
            print('link:',link)
            yield scrapy.Request(link,callback=self.parse_item) # callback:指定数据提取的回调函数

        # 翻页
        if self.offset <=8000:
            self.offset +=30
            yield scrapy.Request(self.url+str(self.offset),callback=self.parse)


    def parse_item(self, response):
        '''
        详情页面，解析投诉条目
        :param response:
        :return:
        '''
        item = SunspiderItem()
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[1]/text()').extract()[0].split('：')[-1]
        item['url'] = response.url
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[2]/text()').extract()[0].split(':')[-1]
        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]/text()').extract()
        item['content'] = ''.join(item['content'])
        tmp = response.xpath('//div[@class="wzy1"]/table[2]//tr[2]/td[@class="txt16_3"]/div/div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        tmp = tmp.split(' ')
        item['author'] =tmp[0].split('：')[-1]
        item['pub_date'] = tmp[1].split('：')[-1] +' '+ tmp[2]
        yield item
        #item['title'] = response.xpath('').extract()[0]

