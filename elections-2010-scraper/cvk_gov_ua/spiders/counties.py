# -*- coding: utf-8 -*-
from cvk_gov_ua.items import County
from base import BaseSpider


class CountiesSpider(BaseSpider):
    name = "counties"

    def start_requests(self):
      initial_urls = [
        'wm00114?pt00_t001f01=800&pxto=0'
      ]

      for url in initial_urls:
        yield self.build_request(url, self.findRegionUrls)

    def findRegionUrls(self, response):
      for row in response.css("table.t2")[1].css("tr")[1:]:
        region_urls = row.css("td")[3].css("a").xpath("@href").extract()
        for region_url in region_urls:
          yield self.build_request(region_url, self.findCountiesUrls)

    def findCountiesUrls(self, response):
      for url in response.css(".a1small").xpath('@href').extract():
        yield self.build_request(url, self.parseCountiesList)

    def parseCountiesList(self, response):
        council = response.css(".p2::text")[0].extract()
        region = response.css(".p1::text")[0].extract()
        for row in response.css("table.t2")[1].css("tr")[1:]:
          result = row.css("td::text")[2].extract()
          party = row.css("td::text")[0].extract()
          yield County(result=result,
                       region=region,
                       party=party,
                       council=council)
