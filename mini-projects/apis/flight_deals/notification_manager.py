from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

TWILIO_SID = os.getenv('SMS_ACCOUNT_ID')
TWILIO_AUTH_TOKEN = os.getenv('SMS_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = os.getenv('SMS_AUTH_TOKEN')
TWILIO_VERIFIED_NUMBER = os.getenv('SMS_VERIFIED')


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
