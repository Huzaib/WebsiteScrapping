# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappingItem


class ScrapSpiderSpider(scrapy.Spider):
    name = 'scrap_spider'
    page_number = 2
    start_urls = [
        'https://edurev.in/course/quiz/attempt/592_Test-Acceleration/c6eb9efe-4caa-4201-8b78-23e41b156589?courseId=592']

    def parse(self, response):
        items = ScrappingItem()
        question = response.css(".questionBtext p").css("::text").extract()

        items['question'] = question

        yield items
