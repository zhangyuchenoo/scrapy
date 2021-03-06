#coding:utf-8
from scrapy import Spider
from scrapy import Request
from scrapy.selector import Selector
from tutorial.items import MovieItem


class MovieSpider(Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/chart"
    ]

    def parse(self, response):
        movies = Selector(response).xpath('//*[@id="content"]/div/div[1]/div/div/table')
        for movie in movies:
            item = MovieItem()
            if movie.xpath(".//a"):
                item['name'] = movie.xpath(".//a/@title").extract()[0].strip()
                item['link'] = movie.xpath(".//a/@href").extract()[0].strip()
                item['score'] = movie.xpath(".//span[re:test(@class,'rating_nums')]/text()").extract()[0].strip()
                print ("%s %s %s" %(item['name'],item['link'],item['score']))
                yield item;

    def start_requests(self):
        yield Request("https://movie.douban.com/chart",headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'})