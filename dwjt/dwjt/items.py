# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DwjtItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tilte = scrapy.Field()
    video = scrapy.Field()
    music_score = scrapy.Field()
