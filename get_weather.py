import requests
import datetime
import datetime

import requests


def weather(s_city, date):
    appid = 'f042797c6712eff724a7bb04089063b5'

    # на несколько дней
    # forecast = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={s_city}&APPID={appid}').json()
    now = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={s_city}&APPID={appid}').json()

    # return round(now['main']['temp'] - 273)
    return round(now['main']['temp_min']) - 273, round(now['main']['temp_max']) - 273, round(now['main']['temp']) - 273

