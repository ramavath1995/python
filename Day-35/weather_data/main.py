import os

import requests
from twilio.rest import Client

twilio_recovery = "CUF3W4HLXSHFYS8XDRAVJHLX"
twilio_account_sid = os.getenv("TW_ACC_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH")
twilio_phone_number = "+17727948395"
api_k = os.getenv("W_KEY")
print(api_k)
key = "c4dae624fdf5080324acf93a1bf9e8c7"
api = "https://api.openweathermap.org/data/2.5/forecast"

weather_para = {
    "lat": 14.696869,
    "lon": 76.854652,
    "appid": key,
    "cnt": 4
}
is_rains = False
response = requests.get(url=api, params=weather_para)
response.raise_for_status()
data = response.json()
for hour_data in data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        is_rains = True
if is_rains:
    client = Client(twilio_account_sid, twilio_auth_token)

    message = client.messages.create(
        from_='+17727948395',
        to='+917396370131',
        body="To day going to rain don't forget umbrella ☂️"
    )

    print(message.status)
