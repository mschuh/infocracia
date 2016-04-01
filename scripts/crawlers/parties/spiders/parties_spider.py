from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.http import Request
from parties.items import PartiesItem

class PartiesSpider(Spider):
    name = "parties-crawler"
    allowed_domains = ["tse.jus.br"]
    start_urls = ["http://filiaweb.tse.jus.br/filiaweb/portal/relacoesFiliados.xhtml"]

    def parse(self, response):
        hxs = Selector(response)
        parties = hxs.xpath('//*[@id="partido"]/option/@value').extract()
        states = hxs.xpath('//*[@id="uf"]/option/@value').extract()
        link = "http://agencia.tse.jus.br/estatistica/sead/eleitorado/filiados/uf/filiados_party_state.zip"
        item = PartiesItem()
        item["parties"] = parties
        item["states"] = states
        item["link"] = link
        yield item
