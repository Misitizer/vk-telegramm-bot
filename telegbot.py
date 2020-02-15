import telebot # это библиотека телеграмма
import data # импорт первых двух лаб
bot = telebot.TeleBot('вместо этой фразы ключ от бота') # подключение бота

telebot.apihelper.proxy = {'https':'https://54.39.24.33:3128'} # подключение Proxy (Роскомнадзор, спасибо). Без прокси не заработает

@bot.message_handler(content_types=['text']) # Бот получает на вход сообщение
def get_text_messages(message):
    if message.text == "Трафик":
        bot.send_message(message.from_user.id, data.net()) # вывод текущего состояния трафика в бота
    elif message.text == "/help":дд
        bot.send_message(message.from_user.id, "Напиши: Трафик или Температура")# подсказка
    elif message.text == "Температура":
        bot.send_message(message.from_user.id, data.temperature()) # вывод текущего состояния темпрературы процесора в бота
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.") # другая подсказка
bot.polling(none_stop=True, timeout=123) # эхо, позволяет слушать запросы боту
