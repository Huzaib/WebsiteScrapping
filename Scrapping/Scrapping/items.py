# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrappingItem(scrapy.Item):
    question = scrapy.Field()
    answer = scrapy.Field()
    trending_questions = scrapy.Field()
    hottest_questions= scrapy.Field()
    unanswered_questions = scrapy.Field()



