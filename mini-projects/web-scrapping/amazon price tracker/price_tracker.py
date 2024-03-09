import smtplib

from bs4 import BeautifulSoup
import requests

USER_AGENT = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 "
              "Safari/537.36")

ACCEPT_HEADER = "en-GB,en-US;q=0.9,en;q=0.8"

tracked_product_url = ("https://www.amazon.com/SAMSUNG-SmartTag2-Bluetooth-Tracker-Tracking/dp/B0CCBXRYRC/?_encoding"
                       "=UTF8&pd_rd_w=5FAE7&content-id=amzn1.sym.034d21de-f825-413a-8c94-7d57d209901e&pf_rd_p"
                       "=034d21de-f825-413a-8c94-7d57d209901e&th=1")


def get_amazon_item_price(item_url):
    options = {
        'User-Agent': USER_AGENT,
        'Accept-Language': ACCEPT_HEADER,
    }
    response = requests.get(url=item_url, headers=options)
    soup = BeautifulSoup(response.content, 'html.parser')
    price = soup.find(class_="a-offscreen").getText()
    price_without_currency = price.split("$")[1]
    return float(price_without_currency)


def send_notification(email_addr, destination, subject, msg, options):
    try:
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email_addr, password=options["emailpw"])
            connection.sendmail(from_addr=email_addr, to_addrs=destination,
                                msg=f'''Subject: {subject}\n\n{msg} ''')

    except smtplib.SMTPException as error:
        print(f'Could not send email due to {error}')
    else:
        print(f'Email sent to {destination}')


target_price = 21

scrapped_price = get_amazon_item_price(tracked_product_url)

if scrapped_price < target_price:
    send_notification(email_addr="fake@gmail.com",
                      destination="myemail@gmail.com",
                      subject="Time To Buy",
                      msg=f'You email is below the target price at ${scrapped_price}',
                      options={}
                      )
