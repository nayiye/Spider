# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from SunSpider.items import SunspiderItem


class Sun3Spider(CrawlSpider):
    name = 'Sun3'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=']

    # 匹配翻页的链接提取器
    page_link = LinkExtractor(restrict_xpaths=('//div[@class="pagination"]/a[text()=">"]',))
    # 匹配详情链接提取器
    content_link = LinkExtractor(restrict_xpaths=('//a[@class="news14"]'))
    rules = [
        Rule(page_link,follow=True), # 翻页的规则
        Rule(content_link,callback='parse_item') # 详情链接处理的规则
    ]

    def parse_item(self, response):
        #print('body:',response.body.decode('gbk','ignore'))
        item = SunspiderItem()
        item['title'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[1]/text()').extract()
        if len(item['title'])>0:
            item['title'] = item['title'][0]
        else:
            item['title'] = '空'
        #[0].split('：')[-1]
        item['url'] = response.url
        item['number'] = response.xpath('//div[@class="wzy1"]/table[1]//tr/td[2]/span[2]/text()').extract()
        if len(item['number'])>0:
            item['number'] = item['number'][0]
        else:
            item['number'] = '空'

        item['content'] = response.xpath('//div[@class="wzy1"]/table[2]//tr[1]/td[@class="txt16_3"]/text()').extract()
        item['content'] = ''.join(item['content'])
        tmp = response.xpath(
            '//div[@class="wzy1"]/table[2]//tr[2]/td[@class="txt16_3"]/div/div[@class="wzy3_2"]/span/text()').extract()[0].strip()
        tmp = tmp.split(' ')
        item['author'] = tmp[0].split('：')[-1]
        item['pub_date'] = tmp[1].split('：')[-1] + ' ' + tmp[2]
        yield item
