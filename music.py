import time
import smbus
# from weather_tts import *
import os
import subprocess
import pygame
pygame.init()
pygame.mixer.init()


b=pygame.mixer.music.get_busy()   #检查音乐流是否在播放



#---
# init
#---
from glob import glob
music_index = 0

# music_dir='/media/arthur/DATA/gaodianzhuo/pi/weather_tts/music'
# mp3_files = glob('/media/arthur/DATA/gaodianzhuo/pi/weather_tts/music/*.mp3')

_dir=os.path.dirname(os.path.abspath(__file__))

playlist_path=os.path.join(_dir,'music')+'/*.mp3'

mp3_files = glob(playlist_path)




#---
# music control
#---
def play(music_file):
    
    try:
        pygame.mixer.music.stop()
    except:
        pass
    
    # for music_file in music_list:

    pygame.mixer.music.load(music_file)
        # pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    return 0



def play(music_list):
    '''error 无法循环播放'''
    
    try:
        pygame.mixer.music.stop()
    except:
        pass
    
    for music_file in music_list:
        print(music_file)

        pygame.mixer.music.load(music_file)
        # pygame.mixer.music.load(file)
        pygame.mixer.music.play()

    return 0


# play(mp3_files)
# play(mp3_files[0])



def stop():

    pygame.mixer.music.stop()

    return 0


if __name__ == '__main__':
    play()











