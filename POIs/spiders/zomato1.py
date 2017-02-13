import scrapy
from geopy.geocoders import Nominatim

from POIs.items import PoisItem

def getGeo_from_address(address):

    try:

        geolocator = Nominatim()
        location = geolocator.geocode(address)
        return location.latitude, location.longitude

    except Exception:

        return 40.76, -73.96

class ZomatoSpider(scrapy.Spider):


    baseUrls = ['https://www.zomato.com/new-york-city/restaurants-in-10065']

    name = "zomato1"
    allowed_domains = ["zomato.com"]
    start_urls = [baseUrls[0]]

    def __init__(self):

        # self.page = 0
        self.baseUrl = 'https://www.zomato.com'
        # super(ZomatoSpider, self).__init__()

    def parse(self, response):

        item_tags = response.xpath('//div[@class="card search-snippet-card  search-card "]')
        print "\n\n\n", len(item_tags), "\n\n\n"

        for item_tag in item_tags:

            item = PoisItem()

            try:

                item['ID_or_URL'] = item_tag.xpath('.//a[@class="result-title hover_feedback zred bold ln24   fontsize0 "]/@href').extract()[0]
                # print item['ID_or_URL']

            except Exception as ex:

                # print ex
                item['ID_or_URL'] = ""

            try:

                item['Name'] = item_tag.xpath('.//a[@class="result-title hover_feedback zred bold ln24   fontsize0 "]/text()').extract()[0]
                # print item['Name']

            except Exception as ex:

                # print ex
                item['Name'] = ""

            try:

                item['Phone'] = item_tag.xpath('.//a[@class="item res-snippet-ph-info"]/@data-phone-no-str').extract()[0]
                # print item['Phone']

            except Exception as ex:

                # print ex
                item['Phone'] = ''

            try:

                item['Address'] = item_tag.xpath('.//div[@class="col-m-16 search-result-address grey-text nowrap ln22"]/text()').extract()[0]
                # print item['Address']

            except Exception:

                item['Address'] = ''

            item['City'] = "New York"

            item['State'] = "NY"

            item['Country'] = "United States"

            item['Postal'] = "10065"

            item['Code'] = ""

            try:
                item['Category'] = item_tag.xpath(
                    './/a[@class="zdark ttupper fontsize6"]/text()').extract()[0]

                # print item['Category']

            except Exception as ex:
                # print ex
                item['Category'] = ''

            # yield item

            # item['Latitude'], item['Longitude'] = getGeo_from_address(item['Address'])

            # item['Latitude'], item['Longitude'] = self.parse_detailPage(item['ID_or_URL'])

            request = scrapy.Request(item['ID_or_URL'],
                                     callback=self.parse_detailPage)
            request.meta['item'] = item

            yield request

            # item['Latitude'] = 40.76
            #
            # item['Longitude'] = -73.96


        xpath_Next_Page = './/a[@class="paginator_item   next item"]/@href'
        if response.xpath(xpath_Next_Page):
            # page = self.page + 1
            url_Next_Page = self.baseUrl + response.xpath(xpath_Next_Page).extract()[0]

            import time
            print "\n\n\n", url_Next_Page, "\n\n\n"
            time.sleep(2)

            request = scrapy.Request(url_Next_Page, callback=self.parse)
            yield request

    # def parse_detailPage(self, link):
    #
    #     response = scrapy.http.Response(str(link))
    #
    #     print  "/n/n/n", link
    #     print response.url, "/n/n/n"
    #
    #     with open('body.txt', 'w') as f:
    #         f.write(response.body)
    #
    #     location = response.xpath('div[@class="resmap-img"]/@data-url').extract()[0]
    #
    #     return location, 0

    def parse_detailPage(self, response):

        # print "\n\n\n", response.url, "\n\n\n"
        #
        # with open('body.txt', 'w') as f:
        #     f.write(response.body)

        # response = scrapy.http.Request(link)

        try:

            latitude = response.xpath('//meta[@itemprop="latitude"]/@content').extract()[0]

        except Exception:

            latitude = ""

        try:

            longitude = response.xpath('//meta[@itemprop="longitude"]/@content').extract()[0]

        except Exception:

            longitude = ""

        item = response.meta['item']
        item['Latitude'] = latitude
        item['Longitude'] = longitude

        yield item