import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
stock_endpoint = os.getenv("STOCK_ENDPOINT")
stock_api_key = os.getenv("STOCK_ALPHA_API_KEY")
news_endpoint = os.getenv("NEWS_ENDPOINT")
news_endpoint_api_key = os.getenv("NEWS_ENDPOINT_API_KEY")


def get_stock_price(stock_name):
    yesterdays_closing = 0
    day_before_yesterday = 0
    difference_percent = 0
    symbol = '🔻'

    if stock_name:
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': stock_name,
            'apikey': stock_api_key
        }
        response = requests.get(url=stock_endpoint, params=params)
        response.raise_for_status()
        response = response.json()['Time Series (Daily)']
        data_list = [value for (key, value) in response.items()]
        yesterdays_closing = float(data_list[0]["4. close"])
        day_before_yesterday = float(data_list[1]["4. close"])
        difference = abs(yesterdays_closing - day_before_yesterday)
        difference_percent = (difference / yesterdays_closing) * 100
        symbol = '🔺' if yesterdays_closing > day_before_yesterday else symbol

    return {
        'yesterday': yesterdays_closing,
        'before_yesterday': day_before_yesterday,
        'difference_percent':  "{:.2f}".format(difference_percent),
        'stock_name': stock_name,
        'symbol': symbol
    }


def get_stock_news(company_name):
    if company_name:
        params = {
            'q': company_name,
            'from': '2024-2-23',
            'sortBy': 'publishedAt',
            'apiKey': news_endpoint_api_key
        }
        response = requests.get(url=news_endpoint, params=params)
        response.raise_for_status()
        articles_top_3 = response.json()['articles'][:3]
        formatted = [f'Headline: {article['title']} \nBrief: {article['description']} \nSource: {article['url']}'
                     for article in articles_top_3]
        return formatted
    else:
        return ''


def get_today_date():
    date = datetime.now()
    today = f'{date.year}-{date.month}-{date.day - 1}'
    return today
