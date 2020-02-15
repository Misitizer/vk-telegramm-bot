import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from VkBot import VkBot
import psutil
import time

token = 'tokens'

def write_msg(user_id, message):
    vk.method('messages.send',{'user_id': user_id, 'message': message, 'random_id':get_random_id()})

def get_random_id():
    return random.getrandbits(31) * random.choice([-1, 1])

def trafic():
    result = round(float(psutil.net_io_counters()[0])/(1024*1024),2)
    result = str(result) + ('Mb') +'\n'
    return result

vk = vk_api.VkApi(token = token)

longpoll = VkLongPoll(vk)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if round(float(psutil.net_io_counters()[0])/(1024*1024),2)>50:
            write_msg(user_id, 'Что-то не так с трафиком: ' + trafic())
            time.sleep(5)
        elif psutil.sensors_temperatures()['coretemp'][0][1]>50:
            write_msg(user_id, 'Что-то не так с температурой' + str(psutil.sensors_temperatures()['coretemp'][0][0]>50))
            time.sleep(5)
        '''if event.to_me:
            print(event.user_id)
            bot = VkBot(event.user_id)
            print(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))
'''
