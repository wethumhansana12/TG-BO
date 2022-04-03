import os
import telebot

bot =telebot.Telebot("5291589471:AAH6pP1DMxbLx-9wSkX00WsTqndVkqSS-Z8")

@bot=message_handler(commands={"start"})
def send_welcome(message)=:
    bot.reply_to(message,"hey i'm bot")
@bot=message_handler(commands={"How"})
def send_message(message):
    bot.send_message(message,"https://t.me/AdobeFreeCrack")