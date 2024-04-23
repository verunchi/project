import json
import telebot
from telebot import types
token = '7123532905:AAHCw-orSkIET0JSmSqPgNHb3rgtwXhGKtA'
bot = telebot.TeleBot(token)

active_department = ''
result = {
    "department": "",
    "lenta": "",
    "vid datchika": "",
    "datchik": "",
    "date": ""
}

def get_data_for_date(message):
    file = open('data_example.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    for i in range(len(data)):
        if data[i]['date'] == message.text:
            result["date"] = message.text
        else:
            message.text = message.text[::-1]
            message.text = message.text.replace('.', '-')
            result['date'] = message.text


@bot.message_handler(content_types=['text'])

def get_message(message):
    if message.text == '/start':

        bot.set_my_commands(
            commands=[
                types.BotCommand('/start', 'Запуск бота'),
                types.BotCommand('/dance', 'Получить танец'),
                types.BotCommand('/bomb', 'Не нажимать')
            ],
            scope=types.BotCommandScopeChat(message.chat.id)
        )

        file = open('data_example.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        keyboard = types.InlineKeyboardMarkup()
        for department in list(data.keys()):
            button = types.InlineKeyboardButton(text=department, callback_data=department)
            keyboard.add(button)
        bot.send_message(message.from_user.id, text='Добро пожаловать!')
        bot.send_message(message.from_user.id, text='Выберите цех, из которого вы хотите получить данные с датчиков', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global active_department

    file = open('data_example.json.json', 'r', encoding='utf-8')
    data = json.load(file)
    file.close()
    keyboard2 = types.InlineKeyboardMarkup()
    for department in list(data[active_department].keys()):
        button1_2 = types.InlineKeyboardButton(text=department, callback_data=department)
        keyboard2.add(button1_2)
    bot.send_message(message.from_user.id, text='Выберите ленту для просмотра', reply_markup=keyboard2)


    if call.data.startswith('Лента'):
        file = open('data_example.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        lentas = []
        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
            elif active_department == data[i]['department']:
                lentas.append(data[i]['lenta'])

        for lenta in lentas:
            if call.data == lenta:
                result['lenta'] = lenta
                bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
                keyboard3 = types.InlineKeyboardMarkup()
                button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
                button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
                button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
                button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
                button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
                keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
                bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)
                break

            # elif call.data == 'лента №2':
            #     bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
            #     keyboard3 = types.InlineKeyboardMarkup()
            #     button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
            #     button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
            #     button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
            #     button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
            #     button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
            #     keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
            #     bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)
            #
            # elif call.data == 'лента №3':
            #     bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
            #     keyboard3 = types.InlineKeyboardMarkup()
            #     button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
            #     button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
            #     button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
            #     button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
            #     button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
            #     keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
            #     bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)
            #
            # elif call.data == 'лента №4':
            #     bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
            #     keyboard3 = types.InlineKeyboardMarkup()
            #     button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
            #     button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
            #     button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
            #     button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
            #     button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
            #     keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
            #     bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)
            #
            # else:
            #     bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
            #     keyboard3 = types.InlineKeyboardMarkup()
            #     button1_3 = types.InlineKeyboardButton(text='Датчик электричества ', callback_data='Датчик электричества')
            #     button2_3 = types.InlineKeyboardButton(text='Датчик воды', callback_data='Датчик воды')
            #     button3_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик давления')
            #     button4_3 = types.InlineKeyboardButton(text='Датчик температуры', callback_data='Датчик температуры')
            #     button5_3 = types.InlineKeyboardButton(text='Датчик давления', callback_data='Датчик температуры')
            #     keyboard3.add(button1_3, button2_3, button3_3, button4_3, button5_3)
            #     bot.send_message(call.from_user.id, text='Выберите вид датчика', reply_markup=keyboard3)

    if call.data.startswith('Датчик'):
        file = open('datchik.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        vidi_datchikov = []
        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
            elif active_department == data[i]['department']:
                vidi_datchikov.append(data[i]['vid datchika'])

        for vid_datchika in vidi_datchikov:
            if call.data == vid_datchika:
                result['vid datchika'] = vid_datchika
                keyboard4 = types.InlineKeyboardMarkup()
                button1_4 = types.InlineKeyboardButton(text='№1', callback_data='№1')
                button2_4 = types.InlineKeyboardButton(text='№2', callback_data='№2')
                button3_4 = types.InlineKeyboardButton(text='№3', callback_data='№3')
                button4_4 = types.InlineKeyboardButton(text='№4', callback_data='№4')
                button5_4 = types.InlineKeyboardButton(text='№5', callback_data='№5')
                keyboard4.add(button1_4, button2_4, button3_4, button4_4, button5_4)
                bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)
                break

            # elif call.data == 'Датчик воды':
            #     keyboard4 = types.InlineKeyboardMarkup()
            #     button1_4 = types.InlineKeyboardButton(text='Датчик №1 ', callback_data='Датчик №1')
            #     button2_4 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
            #     button3_4 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
            #     button4_4 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
            #     button5_4 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
            #     keyboard4.add(button1_4, button2_4, button3_4, button4_4, button5_4)
            #     bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)
            #     break
            #
            # elif call.data == 'Датчик давления':
            #     keyboard4 = types.InlineKeyboardMarkup()
            #     button1_4 = types.InlineKeyboardButton(text='Датчик №1 ', callback_data='Датчик №1')
            #     button2_4 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
            #     button3_4 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
            #     button4_4 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
            #     button5_4 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
            #     keyboard4.add(button1_4, button2_4, button3_4, button4_4, button5_4)
            #     bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)
            #     break
            #
            # elif call.data == 'Датчик температуры':
            #     keyboard4 = types.InlineKeyboardMarkup()
            #     button1_4 = types.InlineKeyboardButton(text='Датчик №1 ', callback_data='Датчик №1')
            #     button2_4 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
            #     button3_4 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
            #     button4_4 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
            #     button5_4 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
            #     keyboard4.add(button1_4, button2_4, button3_4, button4_4, button5_4)
            #     bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)
            #     break
            #
            # else:
            #     bot.send_message(call.from_user.id, text='Вы выбрали ' + call.data)
            #     keyboard4 = types.InlineKeyboardMarkup()
            #     button1_4 = types.InlineKeyboardButton(text='Датчик №1 ', callback_data='Датчик №1')
            #     button2_4 = types.InlineKeyboardButton(text='Датчик №2', callback_data='Датчик №2')
            #     button3_4 = types.InlineKeyboardButton(text='Датчик №3', callback_data='Датчик №3')
            #     button4_4 = types.InlineKeyboardButton(text='Датчик №4', callback_data='Датчик №4')
            #     button5_4 = types.InlineKeyboardButton(text='Датчик №5', callback_data='Датчик №5')
            #     keyboard4.add(button1_4, button2_4, button3_4, button4_4, button5_4)
            #     bot.send_message(call.from_user.id, text='Выберите номер датчика', reply_markup=keyboard4)
            #     break
    if call.data.startswith('№'):
        file = open('datchik.json', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        datchiki = []
        for i in range(len(data)):
            if data[i]['department'] not in departments:
                departments.append(data[i]['department'])
            elif active_department == data[i]['department']:
                datchiki.append(data[i]['datchik'])

        for datchik in datchiki:
            if call.data == datchik:
                result['datchik'] = datchik
        keyboard5 = types.InlineKeyboardMarkup()
        button5_1 = types.InlineKeyboardButton(text='Посмотреть информацию за последние 14 дней', callback_data='Посмотреть информацию')
        button5_2 = types.InlineKeyboardButton(text='Ввести дату самостоятельно', callback_data='Ввести дату')
        keyboard5.add(button5_1, button5_2)
        bot.send_message(call.from_user.id, text='Выберите, как вы хотите получить информацию', reply_markup=keyboard5)

    if call.data.startswith('Ввести дату'):
        bot.send_message(call.from_user.id, text='Введите дату, за которую хотите посмотреть показания гггг-мм-дд')
        bot.register_next_step_handler(call.message, get_data_for_date)

    elif call.data.startswith('Посмотреть'):
        bot.send_message(call.from_user.id, text='Показания за последние две недели: ')
        file = open('datchik.json', 'r', encoding='utf-8')
        datas = json.load(file)
        file.close()
        text = ''
        for data in datas:
            if data['department'] == active_department:
                text += 'Показатели: ' + str(data['value']) + '\n'
        bot.send_message(call.from_user.id, text=text)













bot.polling(none_stop=True, interval=0)