from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, parser='lxml', features="lxml")

article_tag = soup.find(class_='titleline').find('a')
article_text = article_tag.getText()
artile_link = article_tag.get('href')
article_upvote = soup.find(name='span', class_='score').getText()

print(article_tag)
print(article_text)
print(artile_link)
print(article_upvote)
