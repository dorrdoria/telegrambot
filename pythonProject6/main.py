import telebot
from config import keys, TOKEN
from extensions import ConvertionException, APIException


bot = telebot.TeleBot(TOKEN)

@bot.message_handlers(commands=['start', 'help', ])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите коммаду боту в слудующем фоормате: \n<имя валюты> \
<в какую валюту перевести> \
<колличество переводимой валюты>\п Список всех доступных валют: /values'
    bot.reply_to(message, text)

@bot.message_handlers(commands=['values'])
def values(message: telebot.types.Message):
   text = 'Доступные валюты:'
   for key in keys.keys():
      text = '\n'.join((text, key, ))
   bot.reply_to(message, text)


@bot.message_handlers(commands=['text', ])

   try:
      if len(values) != 3:
        raise ConvertionException('Слишком много параметров')

      quote, base, amount = values
      total_base = APIException.convert(quote, base, amount)

   except ConvertionException as e:
       bot.reply_to(message, f'Ошибка пользователя. \n{e}')
   except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

       else:
          text = f'Цена {amount} {quote} в {base} - {total_base}'
          bot.send_message(message, chat.id, text)


bot.polling()
