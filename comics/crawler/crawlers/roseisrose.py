from comics.crawler.crawlers import BaseComicsComComicCrawler

class ComicCrawler(BaseComicsComComicCrawler):
    def _get_url(self):
        self._get_url_helper('Rose Is Rose')
