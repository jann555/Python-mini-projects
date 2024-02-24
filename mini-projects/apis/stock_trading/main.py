from fetchers import stock_fetcher as stock, twilio_fetcher as sms

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


def stock_info_sender(stock_name, company_name):
    stock_data = stock.get_stock_price(stock_name)
    difference = float(stock_data.get('difference_percent'))
    print(f'Stock Data: {stock_data}')

    if difference > 1:
        news_articles = stock.get_stock_news(company_name)
        print(f'News Articles: {news_articles}')
        send_news_articles(stock_data=stock_data, articles=news_articles)


def send_news_articles(stock_data, articles):
    stock_header = f'{stock_data['stock_name']}:{stock_data['symbol']}'
    for article in articles:
        msg = f'{stock_header} \n Headline: {article['title']} \n Brief: {article['description']}\n Source: {article['url']}'
        sms.send_sms(msg)
        print(f'Sent article: {article['title']}')


stock_info_sender(STOCK_NAME, COMPANY_NAME)
