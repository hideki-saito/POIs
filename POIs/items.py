# -*- coding: utf-8 -*-

import scrapy

class PoisItem(scrapy.Item):

    ID_or_URL = scrapy.Field()
    Name = scrapy.Field()
    Phone  = scrapy.Field()
    Address = scrapy.Field()
    City = scrapy.Field()
    State = scrapy.Field()
    Country = scrapy.Field()
    Postal = scrapy.Field()
    Code = scrapy.Field()
    Latitude = scrapy.Field()
    Longitude = scrapy.Field()
    Category = scrapy.Field()
