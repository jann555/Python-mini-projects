import os
from dotenv import load_dotenv
from twilio.rest import Client

# Load ENV Variables
load_dotenv()
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
to_number = os.getenv("TWILIO_TO_NUMBER")
from_number = os.getenv("TWILIO_FROM_NUMBER")


def send_sms(msg):
    client = Client(account_sid, auth_token)
    client.messages \
        .create(body=msg,
                from_=from_number,
                to=to_number
                )
