# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    link = scrapy.Field()
    director = scrapy.Field()
    score = scrapy.Field()
    describ = scrapy.Field()
    action_time = scrapy.Field()