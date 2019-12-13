# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# 案例：人民网分布式爬虫
# http://politics.people.com.cn/GB/1024/index1.html
# 爬取新闻标题，链接，内容，发表时间
import scrapy


class MenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    link = scrapy.Field()
    content = scrapy.Field()
    sh_time = scrapy.Field()

class Blog(scrapy.Item):
    title=scrapy.Field()
    url = scrapy.Field()
    # content = scrapy.Field()
