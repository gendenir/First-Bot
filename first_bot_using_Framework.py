# -*- coding: utf-8 -*-

import conf
import telebot


bot = telebot.TeleBot(conf.token)


@bot.message_handler(func=lambda message: True, content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)