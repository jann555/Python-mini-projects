from datetime import datetime

from send_emails_gmail.birthday_wisher.utils.email_sender import send_email
from send_emails_gmail.birthday_wisher.utils.read_file import CustomFileReader

QUOTES_FILE = '../resources/quotes.txt'
TUESDAY = 1
quotes_file = CustomFileReader(QUOTES_FILE)

email_address = "sample+email@gmail.com"
destination_email = "sample+email+smtplib@gmail.com"

day_of_week = datetime.now().weekday()

message = quotes_file.get_random_line()

if day_of_week == TUESDAY:
    send_email(email_addr=email_address, destination=destination_email, msg=message)
