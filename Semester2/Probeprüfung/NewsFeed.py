import requests
import json

class NewsFeed:
    url: str

    def __init__(self, url):
        self.url = url

    def get_news(self):
        text = requests.get(self.url)
        jsonObj = json.loads(text)
        return jsonObj
    
    def print_titles(self):
        news = self.get_news()
        for item in news:
            print(item['title'])

if __name__ == "__main__":
    news_feed = NewsFeed("http://mynews.ch")
    news_feed.print_titles()