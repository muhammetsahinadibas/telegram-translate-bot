#! /usr/bin/env python
# -*- coding: UTF-8 -*-

import telebot
from googletrans import Translator

translator = Translator()
bot = telebot.TeleBot(" ") # Enter Telegram bot key !!

@bot.message_handler(commands=['start']) 
def send_welcome(message):
	bot.reply_to(message, "Welcome, Type in the word or text you want to translate.")

@bot.message_handler(commands=['help']) 
def send_help(message):
    bot.reply_to(message, "Type in the word or text you want to translate.")

@bot.message_handler(content_types = ['text']) 
def decoder(message):
    data = message.text
    value = translator.translate(text=data, src="en", dest="tr")
    bot.send_message(message.chat.id, value.text) 

bot.polling()

# - Developer: Muhammet Sahin Adibas
# - Twitter: twitter.com/muhammetadibas 
# - Blog: muhammetsahinadibas.com.tr
# - Github: github.com/muhammetsahinadibas 