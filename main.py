import os
import telebot
import requests
from bs4 import BeautifulSoup


API_KEY = os.environ['API_KEY']

bot = telebot.TeleBot(API_KEY, parse_mode=None)
  

def NewsFromBBC():
     
    
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "haha"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    
    article = open_bbc_page["articles"]
 
   
    results = []
     
    for ar in article:
        results.append(ar["title"])
         
    return results


@bot.message_handler(func=lambda message: True)
def test(message):
  if message.text == 'news?':
    news = NewsFromBBC()
    bot.send_message(message.chat.id , f'top news from bbs, here you go {message.from_user.first_name} ')
    for i in range(len(news)):
      bot.send_message(message.chat.id, news[i])
    
  else:
    	bot.reply_to(message, f'aru kei bujdina yrr{message.from_user.first_name}')


  





bot.infinity_polling()
