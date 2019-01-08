# -*- coding: utf-8 -*-
import scrapy
from duan.items import DuanItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IshuoSpider(CrawlSpider):
    name = 'ishuo'
    allowed_domains = ['ishuo']
    start_urls = ['http://stock.10jqka.com.cn/hks/ggydg_list/']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    def parse(self, response):
        print("bengin parse %s"%response)
        for each in response.xpath('//div[@class="content-1200"]/div/div/ul/li'):
            print('earch %s'%each)
            hh = "hahha"
            content = each.xpath("./a")
            print('this is %s %s'%(content, hh));
            i = DuanItem()
            i['content'] = each.xpath("[@class='content']").extract()
            
            i['ahref'] = each.xpath('/a').extract()
            i['info'] = each.xpath("[@class='info']/text()").extract()
            i['span'] = each.xpath('/span').extract()
            return i

        
        
