import scrapy


class DiemSpiderSpider(scrapy.Spider):
    name = "diem_spider"
    allowed_domains = ["vtvapi3.vtv.vn"]
    start_urls = ["https://vtvapi3.vtv.vn"]

    def parse(self, response):
        pass
import scrapy
import json

class DiemSpider(scrapy.Spider):
    name = "diem_spider"
    def start_requests(self):
        base_url = 'https://vtvapi3.vtv.vn/handlers/timdiemthi.ashx?keywords='
        for sbd in list(range(50000001, 50016514  + 1)) + list(range(51000001, 51020308 + 1)) + list(range(52000001, 52012672 + 1)) + list(range(53000001, 53016316 + 1)) + list(range(54000001, 54015067 + 1)) + list(range(55000001, 55012886 + 1)) + list(range(56000001, 56012182 + 1)) + list(range(57000001, 57010935 + 1)) + list(range(58000001, 58009706 + 1)) + list(range(59000001, 59010680 + 1)) + list(range(60000001, 60006413 + 1)) + list(range(61000001, 61010182 + 1)) + list(range(62000001, 62007277 + 1)) + list(range(63000001, 63007704 + 1)) + list(range(64000001, 64007286 + 1)): # Điều chỉnh dải số báo danh theo nhu cầu
            url = f'{base_url}{sbd:08d}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        data = json.loads(response.body)
        for entry in data:
            yield {
                'SOBAODANH': entry.get('SOBAODANH'),
                'TOAN': entry.get('TOAN'),
                'VAN': entry.get('VAN'),
                'NGOAI_NGU': entry.get('NGOAI_NGU'),
                'LY': entry.get('LY'),
                'HOA': entry.get('HOA'),
                'SINH': entry.get('SINH'),
                'SU': entry.get('SU'),
                'DIA': entry.get('DIA'),
                'GIAO_DUC_CONG_DAN': entry.get('GIAO_DUC_CONG_DAN'),
                'MA_MON_NGOAI_NGU': entry.get('MA_MON_NGOAI_NGU'),
            }

