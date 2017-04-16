# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TeacherItem(scrapy.Item):
    upna_id = scrapy.Field()
    name = scrapy.Field()
    email = scrapy.Field()
    telephone = scrapy.Field()
    timetable = scrapy.Field()