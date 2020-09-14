import telepot
token = '1125971838:AAEML7L-5UNPjjgkdeleaZ7OOy6J5kk2HdI'
TelegramBot = telepot.Bot(token)
print (TelegramBot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        TelegramBot.sendMessage(chat_id, "you said '{}' ".format(msg["text"]))
TelegramBot.message_loop(handle)
