# -*- coding: utf-8 -*-
import telebot


token = '561799639:AAFY_F5Z5KyFTsxHVrb4NLgUIiesDelKxS0'


bot = telebot.TeleBot(token)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)