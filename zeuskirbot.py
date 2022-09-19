import telebot
import random
con="5657498315:AAHHcMepCQqBKqgInQYK7CnPrIga4ReOgfY"
from telebot import types

bot = telebot.TeleBot(con)
price = 500


@bot.message_handler(commands=['start'])
def welcome(message):

    # keyboard
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Отмена", callback_data='nice')

    markup.add(item1)
    if(message.from_user.first_name=="test"):
        pass
    else:
        bot.send_message(message.chat.id,
                        "Приветствую , {0.first_name}!\nЯ бот {1.first_name}, пришел забрать твои гроши..".format(
                            message.from_user, bot.get_me()),
                        parse_mode='html')
 
    bot.send_message(message.chat.id,
                     "На сколько месяцев вы хотите оформить подписку?(Напишите количество месяцев цифрами)".format(
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        try:
            value_mounth=int(message.text)
        except:
            pass
        if message.text == 'Отмена':
            
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='good')
            item2 = types.InlineKeyboardButton("Не", callback_data='bad')

            markup.add(item1, item2)
            bot.send_message(message.chat.id, 'Вы уверены, что хотите отменить?', reply_markup=markup)
            
        try:
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Да", callback_data='buy')
            item2 = types.InlineKeyboardButton("Не", callback_data='not_buy')
            markup.add(item1, item2)
            
            result=price*value_mounth
            bot.send_message(message.chat.id, "С вас выйдет " + str(result) + " $", parse_mode='html')
            bot.send_message(message.chat.id, 'Перейти к оплате?', reply_markup=markup )
            
        except:
            bot.send_message(message.chat.id, 'Напишите количество месяцев цифрами\nПример, если хотите три месяца напишите:  3')
   


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да", callback_data='good')
    item2 = types.InlineKeyboardButton("Не", callback_data='bad')

    markup.add(item1, item2)
    
    try:
        if call.message:
            if call.data == 'good':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Bay-bay.\nДля перезапуска бота нажмите /start",
                reply_markup=None)
                bot.stop_polling()
            elif call.data == 'bad':
                welcome(call.message)
            elif call.data =='nice':
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Вы уверены, что хотите отменить?",
                reply_markup=markup)
            elif call.data == 'buy':
                
                markup = types.InlineKeyboardMarkup(row_width=2)
                
                item1 = types.InlineKeyboardButton("Карта", callback_data='visa')
                item2 = types.InlineKeyboardButton("Крипта", callback_data='ckript')
                markup.add(item1, item2)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Выберите способ оплаты", reply_markup=markup)
                
            elif call.data == 'not_buy':
            
                markup = types.InlineKeyboardMarkup(row_width=2)
                
                item1 = types.InlineKeyboardButton("Да", callback_data='good')
                item2 = types.InlineKeyboardButton("Нет", callback_data='bad')
                markup.add(item1, item2)
                
                
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Хотите ли вы уйти", reply_markup=markup)
                
            elif call.data == 'visa':
                bot.send_message(chat_id=call.message.chat.id,  text="https://vk.com/id_66696")
                
                
                
                
            
            elif call.data == 'ckript':
                bot.send_message(chat_id=call.message.chat.id,  text="https://vk.com/id26402077")
            
            
            

            
            

            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                      text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")

    except Exception as e:
        print(repr(e))


# RUN
bot.polling(none_stop=True)
