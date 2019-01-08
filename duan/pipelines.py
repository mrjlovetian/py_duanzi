# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DuanPipeline(object):
    def process_item(self, item, spider):
        print('.....................', item.content)
        db = pymysql.connect('localhost', 'root', '897011805', 'yhj')
        cursor = db.cursor()
        sql = """INSERT INTO duanzi VALUES ('%s', '%s', '%s', '%s')""" %(item.content, item.ahref, item.info, item.span)
        cursor.execute(sql)
        cursor.commit()
        db.close()
        return item
