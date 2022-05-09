#main commands and bot creation
import telebot
from decouple import config
from weather import getCurrentWeather
import time

BOT_TOKEN = config('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

weather = ["الطقس","weather","temp"]
greetings = ["هلو","hi","hey","hello"]
whoAreYou = ["منو" ,"who" ]
botName = "shurukH_bot"
audio = ["شروق"]
audio1= ["تحبني","تحبني؟","تحبني ؟","بتحبني","بتحبني؟","بتحبني ؟"]
@bot.message_handler(commands=["ابدا" , "start" , "يلا"])
def welcome(message):
    bot.send_message(message.chat.id,"❤️​ ياهلا وغلا ❤️​")
    time.sleep(1)
    bot.send_message(message.chat.id,"❤️​ دخيل هالوجه ❤️​ ...َ")
    time.sleep(1)
    bot.send_message(message.chat.id, "😘​ تعالي ابوسك 😘​ ...َ")

#answering every message not just commands 
def isMSg(message):
    return True


@bot.message_handler(func=isMSg)
def reply(message):
    words = message.text.split()
    if words[0].lower() in weather :
        report = getCurrentWeather()
        return bot.send_message(message.chat.id,report or "✋​خطا الطقس غير متوفر الان 😫​ !!")
    if words[0].lower() in whoAreYou :
        return bot.reply_to(message,f"انا❤️​{botName}❤️​")
    if words[0].lower() in greetings :
        time.sleep(1)
        return bot.reply_to(message,"دخيلو انا الي يسال علية !​😍​😘​")
    if words[0].lower() in audio :
        bot.send_audio(chat_id='1227154047', audio=open('//home//blackroot//Desktop//شروق.mp3', 'rb'))
    if words[0].lower() in audio1 :
        bot.send_audio(chat_id='1227154047', audio=open('//home//blackroot//Desktop//تحبني.mp3', 'rb'))
    else:
        return bot.reply_to(message,"that's not a command of mine!")

bot.polling()