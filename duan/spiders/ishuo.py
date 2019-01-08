# -*- coding: utf-8 -*-
import scrapy
from duan.items import DuanItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IshuoSpider(CrawlSpider):
    name = 'ishuo'
    allowed_domains = ['ishuo']
    start_urls = ['https://ishuo.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        for each in response.xpath('//li/div'):
            i = DuanItem()
            i['content'] = each.xpath("[@class='content']").extract()
            i['ahref'] = each.xpath('/a]').extract()
            i['info'] = each.xpath("[@class='info']/text()").extract()
            i['span'] = each.xpath('/span"]').extract()
            return i

        
        
