# -*- coding: utf-8 -*-
import scrapy
from duan.items import DuanItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IshuoSpider(CrawlSpider):
    name = 'ishuo'
    allowed_domains = ['duanziwang.com']
    start_urls = ['http://duanziwang.com/page/2/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        print("bengin parse %s"%response)
        for each in response.xpath('//main/article/div'):
            print('earch %s'%each)
            hh = "hahha"
            content = each.xpath("./h1/a/text()").extract()[0]
            print('this is %s %s'%(content, hh));
            # i = DuanItem()
            # i['content'] = each.xpath("[@class='content']").extract()
            
            # i['ahref'] = each.xpath('/a').extract()
            # i['info'] = each.xpath("[@class='info']/text()").extract()
            # i['span'] = each.xpath('/span').extract()
            # return i

        
        
