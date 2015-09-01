__author__ = 'linliang'

from scrapy.crawler import CrawlerProcess
from douban_movie.spiders.douban import DoubanSpider

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(DoubanSpider)
process.start() # the script will block here until the crawling is finished