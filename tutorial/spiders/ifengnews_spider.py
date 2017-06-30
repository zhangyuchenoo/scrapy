from scrapy import Spider
from scrapy.selector import Selector
from tutorial.items import NewsItem

class NewsSpider(Spider):
      name = "ifeng"
      allowed_domains = ["ifeng.com"]
      start_urls = [
          "http://www.ifeng.com"
      ]
  
      def parse(self,response):
          topNews = Selector(response).xpath('//ul[@class="FNewMTopLis"]/li')
          for news in topNews:
             item = NewsItem()
             if news.xpath('a'):
                 title = news.xpath("a/text()").extract()[0].strip()
                 url = news.xpath("a/@href").extract()[0].strip()
                 item['title'] = title
                 item['url'] = url
                 print("title %s href %s" %(title,url))
                 yield  item

