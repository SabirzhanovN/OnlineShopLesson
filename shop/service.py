import telepot

token = '7166132777:AAGN6uJN05Vvrd2ULKdjXS2nc6p9iYjGTks'
my_chat_id = '1404363032'

telegram_bot = telepot.Bot(token)


def send_message(text):
    telegram_bot.sendMessage(my_chat_id, text)
