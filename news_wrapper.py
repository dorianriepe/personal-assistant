import requests
from bs4 import BeautifulSoup


class NewsScraper:
    __instance = None

    @staticmethod
    def getInstance(feed_url='https://www.tagesschau.de/xml/rss2/'):
        if NewsScraper.__instance is None:
            NewsScraper(feed_url)
        return NewsScraper.__instance

    def __init__(self, feed_url='https://www.tagesschau.de/xml/rss2/'):
        if NewsScraper.__instance is None:
            self.feed_url = feed_url
            NewsScraper.__instance = self
        else:
            raise Exception("This class is a singleton!")

    def setFeedUrl(self, feed_url):
        self.feed_url = feed_url

    def getFeedUrl(self):
        return self.feed_url

    def getArticleList(self):
        article_list = []
        try:
            articles = self._find_articles()
            for a in articles[:5]:
                title = a.find('title').text
                description = a.find('description').text
                article = {
                    'title': title,
                    'description': description
                }
                article_list.append(article)
            return article_list
        except Exception as e:
            print('The scraping job failed. See exception: ')
            print(e)

    def _find_articles(self):
        xml = self._getResponse()
        soup = BeautifulSoup(xml, features='xml')
        articles = soup.findAll('item')
        return articles

    def _getResponse(self):
        r = requests.get(self.feed_url)
        return r.content
