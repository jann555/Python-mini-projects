from fetchers import stock_fetcher as stock, twilio_fetcher as sms

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"


def stock_info_sender(stock_name, company_name):
    stock_data = stock.get_stock_price(stock_name)
    difference = float(stock_data.get('difference_percent'))

    if difference > 5:
        news_articles = stock.get_stock_news(company_name)
        send_news_articles(stock_data=stock_data, articles=news_articles)


def send_news_articles(stock_data, articles):
    stock_header = f'{stock_data['stock_name']}:{stock_data['symbol']}{stock_data['difference_percent']}%'
    for article in articles:
        msg = f'{stock_header} \n{article}'
        sms.send_sms(msg)


stock_info_sender(STOCK_NAME, COMPANY_NAME)
