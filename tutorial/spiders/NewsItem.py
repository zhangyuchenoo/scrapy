import scrapy

class StackItem(scrapy.Item):
     title = scrapy.Field()
     url = scrapy.Field()
