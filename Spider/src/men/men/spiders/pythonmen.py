# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy.spiders.crawl import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from men.items import MenItem


class PythonmenSpider(RedisSpider):
    name = 'pythonmen'
    # allowed_domains = ['people.com']
    # start_urls = ['http://people.com/']
    redis_key = 'ptrhonmen:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(PythonmenSpider, self).__init__(*args, **kwargs)

    # def __init__(self):
        self.url = 'http://politics.people.com.cn/GB/1024/index{}.html'
        self.page = 1
        self.max_page = 7

    def get_url(self):
        return self.url.format(str(self.page))

    def parse_detail(self, response):
        content = response.xpath('//div[@class="box_con"]/p/text()').extract()
        content = ''.join(content)
        print("content:", content)

    def parse(self, response):

        ls = response.xpath('//div[@class="ej_list_box clear"]/ul/li')
        # print(len(ls))
        for i in ls:
            item = MenItem()
            item['title'] = i.xpath('./a/text()').extract()[0].strip()
            item['sh_time'] = i.xpath('./em/text()').extract()[0].strip()
            link= i.xpath('./a/@href').extract()[0].strip()
            item['link']=link
            repon = "http://politics.people.com.cn" + link
            yield item
            yield scrapy.Request(repon, callback=self.parse_detail, dont_filter=True)

            # print(repon)

            # print("title", title)
            # print('time:', time)
            # print("link:" + "http:" + link)
            # print('=' * 600)

        self.page += 1
        if self.page <= self.max_page:
            new_url = self.get_url()
            print("page:", self.page)
            yield scrapy.Request(new_url, callback=self.parse, dont_filter=True)
