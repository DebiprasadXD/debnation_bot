import telebot
import time


bot_token='1403425622:AAGgKJDc8D8BrNnkKYx-Uj38jX7q6yTul9U'

  
bot=telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,"Hi There Pal Welcome🤗       What's up! I can echo your message,type any message 😉🎤")
 
@bot.message_handler(commands=['yt'])
def send_welcome(message):
  bot.reply_to(message,'Visit here!🔥    https://www.youtube.com/channel/UCcMTl3AlK6NSxN8on0tZv_Q')
 
@bot.message_handler(commands=['help'])
def send_welcome(message):
  bot.reply_to(message,'Contact @DebNationXD for support or check my github page: https://github.com/DebiprasadXD/Instantbit_bot                       Thank You 🙏')
  
@bot.message_handler(func=lambda message: True)
def echo_message(message):
  bot.reply_to(message, message.text)
 

while True : 
  send_welcome is not None 
   
  try:
    bot.polling()
  except Expectation:
    time.sleep(25)
   
     
     
    
 
       
     
 
