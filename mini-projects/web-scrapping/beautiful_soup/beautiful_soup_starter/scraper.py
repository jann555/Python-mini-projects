from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/news')

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, parser='lxml', features="lxml")

articles = soup.find_all('a')
article_texts = []
article_links = []

print(articles)

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

article_up_votes = [int(score.getText().split(' ')[0]) for score in soup.find_all(name='span', class_='score')]

print(article_texts)
print(article_links)
print(article_up_votes)
