#-- coding:utf-8 --
import telebot

bot = telebot.TeleBot("TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "向我发送图片/网址就可以啦w")

@bot.message_handler(content_types=["text", "sticker", "photo", "audio"], func=lambda message: True)
def forward_all(message):
	bot.forward_message("-100XXXXXXXXXX", message.chat.id, message.message_id)
bot.polling(none_stop=True)
