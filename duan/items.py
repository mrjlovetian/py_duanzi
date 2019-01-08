# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DuanItem(scrapy.Item):
    content = scrapy.Field()
    ahref = scrapy.Field()
    info = scrapy.Field()
    span = scrapy.Field()
