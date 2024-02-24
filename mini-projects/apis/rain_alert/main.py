import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
API_KEY = os.getenv("API_KEY_OPEN_WEATHER")
to_number = os.getenv("TWILIO_TO_NUMBER")
from_number = os.getenv("TWILIO_FROM_NUMBER")
ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    'lat': 33.748997,
    'lon': -84.387985,
    'appid': API_KEY,
}
client = Client(account_sid, auth_token)

response = requests.get(url=ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    message = client.messages \
        .create(body="It's going to rain today. Bring an umbrella ☔",
                from_=from_number,
                to=to_number
                )
    print(message.status)
