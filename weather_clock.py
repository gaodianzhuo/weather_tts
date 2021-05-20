from datetime import datetime 
import schedule
import time
from weather_tts import *


def speak2():
    
    weather_info = get_weather(101010700)
    print(weather_info)

    # tts(weather_info)

    synthsis = SpeechSynthsis(18000)

    ##### reset test
    mytxt = "北京时间:"+str(datetime.now().hour)+"点整"+str(weather_info)
    synthsis.append(mytxt)

    sleep(20)
    synthsis.close()
    print ('finished')


# speak2()

def job():
    if 6<datetime.now().hour<18:
        print("I'm working...")
        speak()
 
schedule.every().hour.do(job)
 
while True:
        schedule.run_pending()
        time.sleep(10)







# #---
# # 每隔一段时间执行一个函数
# #---

# import schedule
# import time
 
# def job():
#     print("I'm working...")
 
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
 
# while True:
#     schedule.run_pending()
#     time.sleep(1)



# import schedule
# import time
 
# def job(name):
#     print("her name is : ", name)
 
# name = xiaona
# schedule.every(10).minutes.do(job, name)
# schedule.every().hour.do(job, name)
# schedule.every().day.at("10:30").do(job, name)
# schedule.every(5).to(10).days.do(job, name)
# schedule.every().monday.do(job, name)
# schedule.every().wednesday.at("13:15").do(job, name)
 
# while True:
#     schedule.run_pending()
#     time.sleep(1)

