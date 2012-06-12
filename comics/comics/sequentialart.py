from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.core.comic_data import ComicDataBase

class ComicData(ComicDataBase):
    name = 'Sequential Art'
    language = 'en'
    url = 'http://www.collectedcurios.com/'
    start_date = '2005-06-13'
    rights = 'Phillip M. Jackson'

class Crawler(CrawlerBase):
    time_zone = 0

    def crawl(self, pub_date):
        page = self.parse_page(
            'http://www.collectedcurios.com/sequentialart.php')
        url = page.src('img#strip')
        return CrawlerImage(url)