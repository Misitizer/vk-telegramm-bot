import requests, bs4
import psutil


class VkBot:

    def __init__(self, user_id):
        self._USER_ID = user_id
        self._COMMANDS = ["ПРИВЕТ","ПОГОДА","ПОКА","КОМАНДЫ","ТРАФИК"]
        self._USERNAME = self._get_user_name_from_vk_id(user_id)

    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_tag(bs.findAll("title")[0])

        return user_name.split()[0]

    def new_message(self, message):
        if message.upper() == self._COMMANDS[0]:
            return f"Ну здравствуй, {self._USERNAME}!"

        elif message.upper() == self._COMMANDS[1]:
            return self._get_weather()

        elif message.upper() == self._COMMANDS[2]:
            return f"Прощай, {self._USERNAME}!"

        elif message.upper() == self._COMMANDS[3]:
            return f"Команды: привет, погода, пока, команды"
        elif message.upper() == self._COMMANDS[4]:
            return self.trafic()

        else:
            return "Не понимаю о чем вы... Мои команды: привет, погода, пока, команды"

    def _clean_tag(self,strline):
        result = ""
        not_skip = True
        for i in list(strline):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True

        return result

    def _get_weather(city: str = "моска") -> list:
        request = requests.get("https://sinoptik.com.ru/погода-москва")
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        p3 = bs.select('.temperature .p3')
        weather1 = p3[0].getText()
        p4 = bs.select('.temperature .p4')
        weather2 = p4[0].getText()
        p5 = bs.select('.temperature .p5')
        weather3 = p5[0].getText()
        p6 = bs.select('.temperature .p6')
        weather4 = p6[0].getText()

        result = ''
        result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
        result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
        temp = bs.select('.rSide .description')
        weather = temp[0].getText()
        result = result + weather.strip()

        return result

    def trafic(self):
        result = round(float(psutil.net_io_counters()[0])/(1024*1024),2)
        result = str(result) + ('Mb') +'\n'

        return result
