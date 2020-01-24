import requests
import time
import schedule
import datetime
from pandas_datareader import data as pdr

import yfinance as yf
def telegram_bot_sendtext(bot_message):
    bot_token='1061807346:AAGRQUWoN-J4oRf2BwXInqkTVt1NMEehfvM'
    bot_chatID='-233612679'
    send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response=requests.get(send_text)
    print(send_text)
    return response.json()
test=telegram_bot_sendtext("Testing bot")
print(test)
price=''
def getStock():
     #print("here")
     bot_token = '1061807346:AAGRQUWoN-J4oRf2BwXInqkTVt1NMEehfvM'
     bot_chatID = '-233612679'
     response= "Let me fetch Latest quote for you \n"
     symbol='NTAP'
     dt_today = str(datetime.datetime.now())
     dt_today = dt_today.split(" ")
     dt_today_lst = dt_today[0].split("-")
     #print(dt_today[0],dt_today[1],dt_today[2])
     aapl=pdr.get_data_yahoo(symbol,  start=datetime.datetime(int(dt_today_lst[0]), int(dt_today_lst[1]), int(dt_today_lst[2])),
                          end=datetime.datetime(int(dt_today_lst[0]), int(dt_today_lst[1]), int(dt_today_lst[2])))
     print(aapl)
     price=(aapl["Close"][1]).round(2)

     price_int=price
     print(price_int)
     price=str(price)
     price="Current price for "+symbol+ " is"+price
     price=str(price.encode('utf-8','ignore'),errors='ignore')
     send_text='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + price
     #print(send_text)
     if(aapl["Close"][0]==aapl["Close"][1]):
         print("Have a good sleep, That's it for the day")

     elif price_int>60:
        response=requests.get(send_text)
     elif(price_int<55):
         response = requests.get(send_text)



import threading
while True:
    getStock()
    #btcTracker()
    time.sleep(10)