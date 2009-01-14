from comics.crawler.crawlers import BaseComicCrawler

class ComicCrawler(BaseComicCrawler):
    def _get_url(self):
        # FIXME: The uvod feed often contains dates which feedparser fails
        # to parse, like '19 Sept 2008 00:00:00 -0800'

        # TODO: Fetch line of text which sometimes are associated with a strip.

        self.feed_url = 'http://www.macguff.fr/goomi/unspeakable/rss.xml'
        self.parse_feed()

        for entry in self.feed['entries']:
            if (entry['updated_parsed'] is not None and
                self.timestamp_to_date(entry['updated_parsed']) == self.pub_date
                and entry['title'].startswith('Strip #')):
                self.title = entry['summary']
                self.web_url = entry['link']
                break

        if self.web_url is None:
            return

        self.parse_web_page()

        for image in self.web_page.imgs:
            if ('src' in image
                and image['src'].startswith('WEBIMAGES/CARTOON/')):
                self.url = self.join_web_url(image['src'])
                return
