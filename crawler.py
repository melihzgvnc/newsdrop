import requests
from bs4 import BeautifulSoup

URL = "https://www.bbc.co.uk/news"

class BBCCrawler:
    
    def __init__(self):
        
        self.url = URL
        self.news = []
        self.collect_news()
    
    def get_links(self):
        
        response = requests.get(self.url).content
        soup = BeautifulSoup(response, 'html.parser')
        links = soup.find_all('a', class_='exn3ah91')
        
        first_10 = []
        for i in range(10):
            link = links[i].get("href")
            if not 'live' in link:
                first_10.append(link.replace("/news", ""))
        return first_10

    def get_news_content(self, url_extension):
        response = requests.get('https://www.bbc.co.uk/news' + url_extension).content
        soup = BeautifulSoup(response, 'html.parser')
        
        news_content = []
        for el in soup.find_all('p', class_='e1jhz7w10'):
            news_content += el.get_text() + " "
        
        text = "".join(news_content)
        return text

    def collect_news(self):
        links = self.get_links()
        self.news = list(map(self.get_news_content, links))

    @classmethod
    def run(cls):
        instance = cls()
        return instance.news