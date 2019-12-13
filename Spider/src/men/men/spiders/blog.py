# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from scrapy.spiders.crawl import Rule
from scrapy.linkextractors import LinkExtractor
from men.items import Blog


class BlogSpider(RedisCrawlSpider):
    name = 'blog'
    # allowed_domains = ['blog.com']
    # start_urls = ['http://blog.com/']
    redis_key = 'blog:start_urls'

    page_link=LinkExtractor(restrict_xpaths=('//li[@class="SG_pgnext"]/a'))
    content_link=LinkExtractor(restrict_xpaths=('//span[@class="atc_title"]/a'))
    rules = [
        Rule(page_link,follow=True),
        Rule(content_link,callback='parse_content')
    ]

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(BlogSpider, self).__init__(*args, **kwargs)

    def parse_content(self, response):
        item=Blog()
        url=response.url
        title=response.xpath('//h2[@class="titName SG_txta"]/text()').extract()[0].strip()
        item['url']=url
        item['title'] = title
        yield item
