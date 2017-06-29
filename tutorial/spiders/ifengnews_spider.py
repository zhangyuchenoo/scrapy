from scrapy import Spider
from scrapy.selector import Selector
from tutorial.spiders import NewsItem

class NewsSpider(Spider):
      name = "ifeng"
      allowed_domains = ["ifeng.com"]
      start_urls = [
          "http://www.ifeng.com"
      ]
  
      def parse(self,response):
          topNews = Selector(response).xpath('//ul[@class="FNewMTopLis"]/li')
          for news in topNews:
             # print("--- %s" %news) 
             item = NewsItem()
             title = news.xpath("a/text()").extract()[0]
             url = news.xpath("a/@href").extract()[0]
             #item['title'] = title
             #item['url'] = url
             print("title %s href %s" %(title,url))
             #print("title %s" %news.xpath("a/text()")) 
