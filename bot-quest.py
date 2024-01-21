import json
import telebot
from telebot.types import Message, ReplyKeyboardMarkup, KeyboardButton
from quest import content

token = "6353166653:AAGOlkl1vYVUYaqgWZRNxA2XMuRiwrLsPQM" 
bot = telebot.TeleBot(token=token)

data_path_name = 'users.json'

def load_user_data(data_path):
    try:
        with open(data_path, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_user_data(user_data, data_path):
    with open(data_path, 'w+', encoding='utf8') as file:
        json.dump(user_data, file, ensure_ascii=False)
    
def make_keyboard(buttons):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in buttons:
        markup.add(KeyboardButton(i))
    return markup

text_help = """Список доступных команд:
/start - начать/продолжить квест
/help - вывести справочную информацию о боте

А вот основные пояснения по использованию бота:
- После запуска бота вам предлагается прочитать предысторию и ответить на вопрос для продолжения квеста
- Так вы сможете контролировать действия персонажа и менять сюжет
- Вместо клавиатуры у вас появляются специальные кнопки - с помощью них вы выберите подходящий вариант ответа
- Подумайте, какой вариант ответа вы бы выбрали и нажмите на соответсвующую кнопку"""

options = sum([i["buttons"] for i in content.values()], []) # список всех возможных команд (для указания пользователю на ошибку при вводе)

@bot.message_handler(commands=['help'])
def say_help(message: Message):
    bot.send_message(message.from_user.id, text_help)

@bot.message_handler(commands=['start'])
def start(message: Message):
    user_data = load_user_data(data_path_name)
    user_id = str(message.from_user.id)
    bot.send_message(user_id, 'Привет! Это квест "Путешествие по подземелью"')
    if user_id in user_data:
        bot.send_message(user_id, 'Вы уже заходили в бота.')
        user_result = user_data[user_id]['result']
        if not user_result:
            bot.send_message(user_id, 'Вы не проходили ни одной развилки. Давайте начнём!')
            markup = make_keyboard(content["start"]["buttons"])
            bot.send_photo(user_id,  photo=open(content["start"]["img"], 'rb'))
            bot.send_message(user_id, content["start"]['text'], reply_markup=markup)
        else:
            bot.send_message(user_id, 'Давайте продолжим!')
            markup = make_keyboard(content[user_result]['buttons'])
            bot.send_photo(user_id,  photo=open(content[user_result]["img"], 'rb'))
            bot.send_message(user_id, content[user_result]['text'], reply_markup=markup)
    else:
        user_data[user_id] = {'name': message.from_user.first_name, 'result': ""}
        save_user_data(user_data, data_path_name)
        bot.send_message(user_id, 'Вы не проходили ни одной развилки. Давайте начнём!')
        markup = make_keyboard(content["start"]["buttons"])
        bot.send_photo(user_id,  photo=open(content["start"]["img"], 'rb'))
        bot.send_message(user_id, content["start"]['text'], reply_markup=markup)
        
@bot.message_handler(content_types=['text'])
def text(message):
    global options
    user_id = str(message.from_user.id)
    user_data = load_user_data(data_path_name)
    user_data[user_id]['result'] = message.text
    user_result = user_data[user_id]['result']
    if message.text in options:
        score = content[user_result]['result']
        markup = make_keyboard(content[user_result]['buttons'])
        bot.send_photo(user_id,  photo=open(content[user_result]["img"], 'rb'))
        bot.send_message(user_id, content[user_result]['text'], reply_markup=markup)
        if score == -1:
            # user_data[user_id]['result'] = message.text
            pass
        elif score == 0:
            markup = make_keyboard(['/start', '/help'])
            bot.send_message(user_id, 'Вы проиграли. Но не расстраивайтесь из-за проигрыша. Вы можете начать квест заново.', reply_markup=markup)
            user_data[user_id]['result'] = []
        elif score == 1:
            markup = make_keyboard(['/start', '/help'])
            bot.send_message(user_id, 'Вы выиграли. Поздравляем! Не желаете перепройти?', reply_markup=markup)
            user_data[user_id]['result'] = []
        save_user_data(user_data, data_path_name)
    else:
        bot.send_message(message.from_user.id, 'Таких команд я пока не изучал. Воспользуйтесь /help, чтобы убедиться, что вы делаете всё верно.')
    
bot.polling()
