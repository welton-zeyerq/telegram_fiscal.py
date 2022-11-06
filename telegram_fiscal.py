#!/usr/bin/env python3
import sys
try:
    import telebot
except:
    sys.exit("Install missing library: pip install pytelegrambotapi")

api_key = ("insert your key")
bot = telebot.TeleBot(api_key)

try:
    def check(message):
        print("new message from: ", message.chat.username)
        print("")
        print("username: ", message.chat.username)
        print("name: ", message.chat.first_name)
        print("id: ", message.chat.id)
        print("date: ", message.date)
        print("text: ", message.text)
        print("type: ", message.chat.type)
        print("are you bot?: ", message.from_user.is_bot)
        print("language_code: ", message.from_user.language_code)
        print("is_automatic_forward: ", message.is_automatic_forward)
        print("")
        return True
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass

try:
    @bot.message_handler(func=check)
    def responder(message):
        text = "your information: \n\n"
        text2 = "\n"
        bot.reply_to(message, text 
        + "username: "+ message.chat.username + text2 
        + "name: "+ message.chat.first_name + text2
        + "id: "+ str(message.chat.id) + text2
        + "date: "+ str(message.date) + text2
        + "type: "+ message.chat.type + text2
        + "text: "+ message.text + text2
        + "are you bot? "+ str(message.from_user.is_bot) + text2
        + "language_code: "+ message.from_user.language_code + text2
        + "is_automatic_forward: "+ str(message.is_automatic_forward))
    bot.polling()
except KeyboardInterrupt:
    sys.exit()
except Exception as error:
    print(error)
    pass
