import telebot
from config import TOKEN, keys
from class_exchange import ConversionException, Converter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help_start(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту через пробел в формате:\n<имя валюты>  \
<в какую валюту перевести>  \
<количество переводимой валюты>\n\n Увидеть список всех валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступная валюта:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))

    bot.reply_to(message, text)


@bot.message_handler(content_types='text', )
def convert(message: telebot.types.Message):

    try:
        money = message.text.split(' ')
        if len(money) != 3:
            raise ConversionException(f'Неправильно введены параметры.')

        quote, base, amount = money

        text = Converter.convert(quote.title(), base.title(), amount)
    except ConversionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:

        bot.send_message(message.chat.id, text)


bot.polling()
