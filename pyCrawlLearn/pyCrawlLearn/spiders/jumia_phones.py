# -*- coding: utf-8 -*-
import scrapy


class JumiaPhonesSpider(scrapy.Spider):
    name = 'jumia_phones'
    allowed_domains = ['https://www.jumia.co.ke/']
    start_urls = ['https://www.jumia.co.ke/smartphones/?price=35000-80000/']

    def parse(self, response):
        # Show which url is being scraped
        print("Crawling data from " + response.url)

        # Extracting data
        productTitle = response.xpath(
            '//div[@class = "sku"]/span[@class = "name"]/text()').extract()

        productPrice = response.xpath(
            '//div[@class = "price-container"]/span[@class = "price"]/text()').extract()

        productRatings = response.xpath(
            '//div[@class = "total-ratings"]/text()').extract()

        dataCategories = zip(productTitle, productPrice, productRatings)

        # Arranging the data
        for item in dataCategories:
            # Create a dictionary and place the results in it
            dataScraped = {
                'site': response.url,
                'productTitle': item[0],
                'productPrice': item[1],
                'productRatings': item[2],
            }

            # Pass data
            yield dataScraped
