# -*- coding: utf-8 -*-
import scrapy
from duan.items import DuanItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IshuoSpider(CrawlSpider):
    name = 'ishuo'
    allowed_domains = ['ishuo']
    start_urls = ['https://ishuo.cn/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        print("bengin parse")
        for each in response.xpath('//ul/li'):
            print('earch %s'%each)
            content = each.xpath("./div[@class='content']/text()")
            print('this is %s'%content);
            i = DuanItem()
            i['content'] = each.xpath("./div[@class='content']").extract()
            
            i['ahref'] = each.xpath('./div/a').extract()
            i['info'] = each.xpath("./div[@class='info']/text()").extract()
            i['span'] = each.xpath('./div/span').extract()
            return i

        
        
