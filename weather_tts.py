#coding=utf-8
from offline_speech.SpeechSynthsis import SpeechSynthsis

import sys
from time import ctime, sleep
import re
import json
import time
import smtplib
import requests
from lxml import etree
from pprint import pprint
from email.header import Header
from email.mime.text import MIMEText


def get_agent():
    import random
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    return random.choice(user_agent_list)



def get_weather(city_id):
    url1 = "http://d1.weather.com.cn/sk_2d/{}.html?_=1544842784069".format(city_id)
    # ??????User-Agent?????????????????????????????????????????????UA
    while 1:
        headers = {
            "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
            "User-Agent": get_agent()
        }
        res1 = requests.get(url1, headers=headers)
        if not re.search('FlashVars', res1.text):
            break
    res1.encoding = "utf-8"
    js = json.loads(res1.text.lstrip('var dataSK = '))
    url2 = "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id)

    print(url2)
    # ??????User-Agent?????????????????????????????????????????????UA
    while 1:
        headers = {
            "Referer": "http://www.weather.com.cn/weather1d/{}.shtml".format(city_id),
            "User-Agent": get_agent()
        }
        res2 = requests.get(url2, headers=headers)
        if not re.search('FlashVars', res2.text):
            break
    res2.encoding = "utf-8"
    s = etree.HTML(res2.text)
    info1 = s.xpath('//*[@class="li1 hot"]/p/text()')[0]  # ???????????????
    info2 = s.xpath('//*[@id="chuanyi"]/a/p/text()')[0]  # ????????????
    # info3 = s.xpath('//*[@class="li4 hot"]/p/text()')[0]  # ????????????

    print(js)
    weather_info = {
        # "??????": js['cityname'],
        "??????": js['date'],
        "??????": js['weather'],
        "??????": js['temp'] + '???',
        "??????": js['WD'],
        "????????????": js['WS'],
        # "????????????": js['SD'],
        "????????????": js['aqi_pm25'],
        # "???????????????": info1,
        "????????????": info2
        # "????????????": info3
    }
    pprint(weather_info)  # ???????????????Json????????????

    return weather_info

# http://www.weather.com.cn/weather1d/101010700.shtml



def main():
    synthsis = SpeechSynthsis(16000)

    ##### reset test
    synthsis.append("??????????????????,123.78.88,????????????????????????????????????????????????????????????,?????????????????????????????????")
    i = 0 
    while True:
        i = i + 1
        if i == 11:
            synthsis.reset()
            print ("reset")
            synthsis.append("????????????,??????????????????")
        sleep(1)
        
        if synthsis.playing():
            print ('playing...')
        
        if i == 15:
            print ("add")
            synthsis.append("?????????????????????")

        if i > 20 and synthsis.dataEmpty():
            break
        pass

    #### performance test

    # synthsis.append("??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ")
    # i = 0
    # while True:
    #     if i < 100:
    #         i += 1
    #         synthsis.append("??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????,")
    #     sleep(1)

    synthsis.close()
    print ('finished')

    return

def tts(message):
    synthsis = SpeechSynthsis(10000)

    ##### reset test
    synthsis.append(str(message))
    # i = 0 
    # while True:
    #     i = i + 1
    #     if i == 11:
    #         synthsis.reset()
    #         print ("reset")
    #         synthsis.append("????????????,??????????????????")
    #     sleep(1)
        
    #     if synthsis.playing():
    #         print ('playing...')
        
    #     if i == 15:
    #         print ("add")
    #         synthsis.append("?????????????????????")

    #     if i > 20 and synthsis.dataEmpty():
    #         break
    #     pass

    #### performance test

    # synthsis.append("??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ")
    # i = 0
    # while True:
    #     if i < 100:
    #         i += 1
    #         synthsis.append("??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????, ??????????????????,")
    #     sleep(1)

    synthsis.close()
    print ('finished')

    return


if __name__ == '__main__':


    weather_info = get_weather(101010700)
    print(weather_info)

    # tts(weather_info)

    synthsis = SpeechSynthsis(18000)

    ##### reset test
    synthsis.append(str(weather_info))

    sleep(20)
    synthsis.close()
    print ('finished')




