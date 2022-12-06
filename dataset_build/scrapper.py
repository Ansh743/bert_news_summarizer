import requests
from bs4 import BeautifulSoup


class Scrapper:
    def __init__(self) -> None:
        self.url = ''
        self.page = None
        self.soup = None
        self.result = None
        self.response = None
        self.status = None

    def setUrl(self, url):
        self.url = url
        self.status = self.__getpage__()
        return self.status

    def __makeSoup__(self):
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def __getpage__(self):
        self.response = requests.get(self.url)
        if self.response.status_code == 200:
            self.__makeSoup__()
        else:
            return 404
        return 200

    def getArticle(self):
        if self.status != 200:
            return None

        results = self.soup.find('article')
        if results:
            self.article = results.text
            return self.article
        
        results = self.soup.find('div', class_='article')
        if results:
            self.article = results.text
            return self.article

        results = self.soup.find('div', class_='article-content')
        if results:
            self.article = results.text
            return self.article
        
        results = self.soup.find('div', class_='story')
        if results:
            self.article = results.text
            return self.article
        
        return None
    
    def canGetArticles(self):
        if self.status != 200:
            return None

        results = self.soup.find('article')
        if results:
            return True
        
        results = self.soup.find('div', class_='article')
        if results:
            return True

        results = self.soup.find('div', class_='article-content')
        if results:
            return True
        
        return False