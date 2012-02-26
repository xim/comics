from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

from lxml import html
import html2text

html2text.BODY_WIDTH = 0
html2text.SKIP_INTERNAL_LINKS = True
html2text.UNICODE_SNOB = True


class Meta(MetaBase):
    name = 'Romantically Apocalyptic'
    language = 'en'
    url = 'http://www.romanticallyapocalyptic.com/'
    rights = 'Vitaly S. Alexius'

class Crawler(CrawlerBase):
    history_capable_days = None
    schedule = None
    time_zone = -5

    def crawl(self, pub_date):
        page = self.parse_page('http://www.romanticallyapocalyptic.com/')
        urls = page.src('img[src*="/art/"]', allow_multiple=True)
        title = None
        text = html.tostring(page._select('div.stand_high')).strip()
        if text:
            text = html2text.html2text(text).strip()

        for url in urls:
            if 'thumb' not in url:
                return CrawlerImage(url, title, text)
