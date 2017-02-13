import scrapy

from POIs.items import PoisItem

zipcode = [10065, 43215, 04101]

def getInfo_from_address(zipcode):
    pass


class ZomatoSpider(scrapy.Spider):

    baseUrls = ['https://www.zomato.com/new-york-city/restaurants-in-10065']
    print 'zomato'

    name = "zomato"
    allowed_domains = ["zomato.com"]
    start_urls = [baseUrls[0]]

    def parse(self, response):

        pageNo = 1

        links = []

        items = response.xpath('//div[@class="card search-snippet-card  search-card "]')
        print "\n\n\n", len(items), "\n\n\n"

        for item in items:
            address = item.xpath('.//div[@class="col-m-16 search-result-address grey-text nowrap ln22"]/text()').extract()[0]
            print address

            links.append(item.xpath('.//a[@class="result-title hover_feedback zred bold ln24   fontsize0 "]/@href').extract()[0])

        print len(links)


        yield scrapy.Request(links[0], callback=self.parse_dir_contents)

        # for link in links:
        #     yield scrapy.Request(link, callback=self.parse_dir_contents)


    # print links, len(links)

        # for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
        #     url = response.urljoin(href.extract())
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):

        item = PoisItem()

        item['ID_or_URL'] = response.url
        print item['ID_or_URL']

        try:
            item['Name'] = "".join(response.xpath("//h1[@class='res-name left mb0']//text()").extract()).replace("\n", "").strip()
            print item['Name']
        except Exception:
            item['Name'] = ""

        try:
            item['Phone'] = "".join(response.xpath("//span[@class='tel']/text()").extract()).replace("\n", "").strip()
            print item['Phone']
        except Exception:
            item['Phone'] = ''
        try:
            item['Address'] = "".join(response.xpath("//div[@class='borderless res-main-address']//text()").extract()).replace("\n", "").strip()
            print item['Address']
        except Exception:
            item['Address'] = ""

        # item['City'] = response.xpath("//span[@class='tel']/text()").extract()
        # print item['City']
        #
        # item['State'] = response.xpath("//span[@class='tel']/text()").extract()
        #
        # item['Country'] = response.xpath("//span[@class='tel']/text()").extract()
        # item['Postal'] = response.xpath("//span[@class='tel']/text()").extract()
        # item['Code'] = response.xpath("//span[@class='tel']/text()").extract()
        # item['Latitude'] = response.xpath("//span[@class='tel']/text()").extract()
        # item['Longitude'] = response.xpath("//span[@class='tel']/text()").extract()
        # item['Category'] = response.xpath("//span[@class='tel']/text()").extract()





        # for sel in response.xpath('//ul/li'):
        #     item = PoisItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item