# -*- coding: utf-8 -*-
import scrapy
from ..items import ScrappingItem


class ScrapSpiderSpider(scrapy.Spider):
    name = 'scrap_spider'
    page_number = 2
    start_urls = ['https://www.answers.com/t/literature-and-language/best?page=1']


    def parse(self, response):
        items = ScrappingItem()
        question = response.css(".a133").css("::text").extract()
        answer = response.css("#inner-gutters .a129").css("::text").extract()
        trending_questions = response.css(".ad_unit_right_1+ .a326 .a129").css("::text").extract()
        hottest_questions = response.css(".ad_unit_right_2+ .a326 .a129").css("::text").extract()
        unanswered_questions = response.css(".ad_unit_right_3+ .a326 .a129").css("::text").extract()

        items['question'] = question
        items['answer'] = answer
        items['trending_questions'] = trending_questions
        items['hottest_questions'] = hottest_questions
        items['unanswered_questions'] = unanswered_questions

        yield items

        next_page = "https://www.answers.com/t/literature-and-language/best?page="+str(ScrapSpiderSpider.page_number)
        if ScrapSpiderSpider.page_number <= 3:
            ScrapSpiderSpider.page_number +=1
            yield response.follow(next_page, callback = self.parse)



