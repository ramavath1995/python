import requests
import os
from twilio.rest import Client

COMPANY_NAME = "APPLE.INC"
STOCK_NAME = "AAPL"

STOCK_PRICE_API = "https://www.alphavantage.co/query"
STOCK_PRICE_API_KEY = "PC6QG1K1G3BT8IBH"
NEWS_API = "https://newsapi.org/v2/everything"
NEW_NEWS_API_KEY = "fa836c0574ad492cb4c5b7c3eaddc25a"
NEWS_API_KEY = "80112072af1d460cb8d013750d47d806"

twilio_account_sid = "ACc423bf73e2197217bd0dac1eb8152392"
twilio_auth_token = "7ac8179422a7e86cde85627f02f83aad"
twilio_phone_number = "+17727948395"

price_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_PRICE_API_KEY,
}

response = requests.get(url=STOCK_PRICE_API, params=price_parameters)
response.raise_for_status()
data = response.json()
new_data = data["Time Series (Daily)"]
data_list = [value for (key, value) in new_data.items()]
yesterday_closing_price = data_list[0]["4. close"]
before_yesterday_closing_price = data_list[1]["4. close"]
print(before_yesterday_closing_price)
print(yesterday_closing_price)

difference = float(yesterday_closing_price) - float(before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"
percentage_diff = round(difference / float(yesterday_closing_price)) * 100
print(percentage_diff)
if abs(percentage_diff) < 2:
    news_parameters = {
        "apiKey": NEW_NEWS_API_KEY,
        "q": COMPANY_NAME,
    }

    a = requests.get(url=NEWS_API, params=news_parameters)
    a.raise_for_status()
    article = a.json()
    my_a = article["articles"]
    list_articles = [f"Headline: {a['title']}.\nBrief{a['description']}" for a in my_a]
    for art in list_articles:
        client = Client(twilio_account_sid, twilio_auth_token)

        message = client.messages.create(
            from_=twilio_phone_number,
            to='+917396370131',
            body=f"{COMPANY_NAME} {up_down}%\n{art}"
        )
