from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase


class ComicData(ComicDataBase):
    name = 'Kellermannen'
    language = 'no'
    url = 'http://www.dagbladet.no/tegneserie/kellermannen/'
    rights = 'Martin Kellerman'


class Crawler(CrawlerBase):
    history_capable_days = 30
    schedule = 'Mo,We,Fr'
    time_zone = 'Europe/Oslo'

    def crawl(self, pub_date):
        epoch = self.date_to_epoch(pub_date)
        url = (
            'http://www.dagbladet.no/tegneserie/' +
            'kellermannenarkiv/serve.php?%d' % epoch)
        return CrawlerImage(url)
