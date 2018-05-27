# -*- coding: utf-8 -*-

import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowd_domains =["http://www.itcast.cn/"]
    start_urls =["http://www.itcast.cn/channel/teacher.shtml#"]
    def parse(self, response):
        # with open("teacher.html","w") as f:
        #     f.write(response.body)
        teacher_list = response.xpath('//div[@class="li_txt"]')
        teacherItem =[]
        for each in teacher_list:

            item = ItcastItem()

            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()
            item["name"] = name[0]
            item["title"] = title[0]
            item["info"] = info[0]
            yield item
            # teacherItem.append(item)

        # return teacherItem