STOCK = "RELIANCE"
COMPANY_NAME = "RELIANCE INDUSTRIES LTD"

account_sid = ' '
auth_token = ' '

NEWS_API = " "
STOCK_API = " "

mobile_number = " "
app_generated_number = " "
import requests
import datetime
from twilio.rest import Client
today = datetime.date.today()
yesterday_date = str(today - datetime.timedelta(days=1))
day_before_yesterday = str(today - datetime.timedelta(days=2))


new = requests.get(url=f"https://newsapi.org/v2/everything?q=reliance&apiKey={NEWS_API}")
news = new.json()
new.raise_for_status()
news_headline = news["articles"][0]["title"]

stock = requests.get(
    url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=RELIANCE.BSE&outputsize=full&apikey={STOCK_API}")
stocks_tesla = stock.json()
stock_yesterday = float(stocks_tesla["Time Series (Daily)"][yesterday_date]["4. close"])
day_before_yesterday_stock = float(stocks_tesla["Time Series (Daily)"][day_before_yesterday]["4. close"])


deflection = round(stock_yesterday-day_before_yesterday_stock,2)

percentage = round((deflection/stock_yesterday)*100,2)

up_down = ""
if percentage > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

client = Client(account_sid, auth_token)
message = client.messages \
        .create(
        body=f"\nCompany name:{STOCK}\n{percentage}{up_down}\nHeadline:\n{news_headline}",
        from_=app_generated_number,
        to= mobile_number
    )
print(message.sid)
