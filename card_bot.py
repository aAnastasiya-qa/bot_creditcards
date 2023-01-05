# подключение библиотек
# В google colab добавить: !pip install pyTelegramBotAPI
# В google colab добавить: !pip install Faker
# для установки необходимо в файл requirements.text добавить строки
# 'PyTelegramBotApi'
# 'faker'

from telebot import TeleBot, types
from faker import Faker


bot = TeleBot(token='введите ваш токен', parse_mode='html') 
faker = Faker() 
card_type_keybaord = types.ReplyKeyboardMarkup(resize_keyboard=True)

card_type_keybaord.row(
    types.KeyboardButton(text='VISA'),
    types.KeyboardButton(text='Mastercard'),
)

card_type_keybaord.row(
    types.KeyboardButton(text='Maestro'),
    types.KeyboardButton(text='JCB'),
)


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    bot.send_message(
        chat_id=message.chat.id, 
        text='Пc! Карта нужна?\nВыбери тип карты:', 
        reply_markup=card_type_keybaord,
    )


@bot.message_handler()
def message_handler(message: types.Message):

    if message.text == 'VISA':
        card_type = 'visa'
    elif message.text == 'Mastercard':
        card_type = 'mastercard'
    elif message.text == 'Maestro':
        card_type = 'maestro'
    elif message.text == 'JCB':
        card_type = 'jcb'
    else:
        
        bot.send_message(
            chat_id=message.chat.id,
            text='Не понимаю тебя :(',
        )
        return


    card_number = faker.credit_card_number(card_type)
  
    bot.send_message(
        chat_id=message.chat.id,
        text=f'Тестовая карта {card_type}:\n<code>{card_number}</code>'
    )


def main():
    
    bot.infinity_polling()


if __name__ == '__main__':
    main()
