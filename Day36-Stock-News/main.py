import requests
import re
import os

# Removing html tags from string
TAG_RE = re.compile(r'<[^>]+>')


def remove_tags(text):
    return TAG_RE.sub('', text)


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
key_alpha = "BOT1UYKGJKEQQOLX"
url_alpha = "https://www.alphavantage.co/query"

params_alpha = {
    "symbol": STOCK,
    "function": "TIME_SERIES_DAILY",
    "apikey": key_alpha,
}

resp_stock = requests.get(url_alpha, params=params_alpha)
data_list = list(resp_stock.json()['Time Series (Daily)'])
today_closing = float(resp_stock.json()['Time Series (Daily)'][data_list[0]]['4. close'])
yesterday_closing = float(resp_stock.json()['Time Series (Daily)'][data_list[1]]['4. close'])

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
key_newsapi = "1e04620e1e404d67ba31fdf7f2b52c83"
url_newsapi = "https://newsapi.org/v2/everything"

params_news = {
    "q": COMPANY_NAME,
    "sortBy": "popularity,publishedAt",
    "apiKey": key_newsapi
}

news = requests.get(url_newsapi, params=params_news)
news.raise_for_status()
news_pieces = [{"headline": n["title"], "brief": n["description"]} for n in (news.json()['articles'])]

# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
per_increase = (today_closing - yesterday_closing) / yesterday_closing
if per_increase > 0:
    message = f"TSLA: 🔺{round(per_increase, 3)}%"
else:
    message = f"TSLA: 🔻{abs(round(per_increase, 3))}%"

for item in news_pieces[:2]:
    message += f"\nHeadline: {item['headline']}\nBrief: {item['brief']}"


# Sending mesaage

bot_token = os.environ.get("telegram_token")
bot_chatID = '783697214'
send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
            '&parse_mode=Markdown&text=' + remove_tags(message)

msg_send = requests.get(send_text)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
