import telebot
import time
from decouple import config
  
bot=telebot.TeleBot(config('BOT_TOKEN'))

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,"Hi There😃 Welcome!🤗.......I can echo your message,type any message 😉🎤")
 
@bot.message_handler(commands=['yt'])
def send_welcome(message):
  bot.reply_to(message,'Visit here!..... https://www.youtube.com/channel/UCcMTl3AlK6NSxN8on0tZv_Q')
 
@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message,'Contact my piro owner❤️😂... @DebNationXD for any support that you need...........Thank You 🙏')
  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  bot.reply_to(message, message.text)
 

while True : 
  send_welcome is not None 
   
  try:
    bot.polling()
  except Expectation:
    time.sleep(25)

