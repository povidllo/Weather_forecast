import json

import requests
def weather(s_city, day):
    appid = 'f042797c6712eff724a7bb04089063b5'

    #на несколько дней
    res = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={s_city}&APPID={appid}').json()

    # return f'Сейчас {int(res["main"]["temp"]) - 273}°С'
    # return res['list'][day]['main']['temp']
    return json.dumps(res, indent=4)
    # return res
print(weather('nizhnevartovsk', 0))




