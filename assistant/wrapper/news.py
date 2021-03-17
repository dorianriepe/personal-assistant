import requests
from bs4 import BeautifulSoup


class NewsScraper:
    __instance = None

    @staticmethod
    def getInstance():
        if NewsScraper.__instance is None:
            NewsScraper()
        return NewsScraper.__instance

    def __init__(self):
        if NewsScraper.__instance is None:
            NewsScraper.__instance = self
        else:
            raise Exception("This class is a singleton!")


    def getArticleList(self, feed_url):
        article_list = []
        try:
            articles = self.__find_articles(feed_url)
            for a in articles[:5]:
                title = a.find('title').text
                description = a.find('description').text
                link = a.find('link').text
                article = {
                    'title': title,
                    'description': description,
                    'link': link
                }
                article_list.append(article)
            return article_list
        except Exception as e:
            print('The scraping job failed. See exception: ')
            print(e)

    def __find_articles(self, feed_url):
        xml = self.getResponse(feed_url)
        soup = BeautifulSoup(xml, features='xml')
        articles = soup.findAll('item')
        return articles

    def getResponse(self, feed_url):
        r = requests.get(feed_url)
        return r.content


