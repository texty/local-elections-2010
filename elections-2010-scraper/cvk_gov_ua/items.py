# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Municipal(scrapy.Item):
    result = scrapy.Field()
    party = scrapy.Field()
    council = scrapy.Field()
    region = scrapy.Field()

class County(scrapy.Item):
    result = scrapy.Field()
    party = scrapy.Field()
    council = scrapy.Field()
    region = scrapy.Field()

