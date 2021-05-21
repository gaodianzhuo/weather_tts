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





#---
# 
#---
复制代码
import pygame,time

pygame.init()
screen = pygame.display.set_mode((196, 100))
pygame.display.set_caption("pygame.mouse函数")

pygame.mixer.music.load('酒醉的蝴蝶.mp3')  #载入音乐
#音乐可以是ogg、mp3、wav等格式
#载入的音乐不会全部放到内容中，而是以流的形式播放的，即在播放的时候才会一点点从文件中读取

pygame.mixer.music.play()  #播放载入的音乐
#该函数立即返回，音乐播放在后台进行。play方法还可以使用两个参数
#如果音乐已经播放，它就会重新启动
#play(loops=0, start=0.0) -> None
#参数1:控制音乐播放的次数。播放(5)将使音乐播放一次，然后重复5次，总共是6次。如果循环是-1，那么音乐就会无限重复
#起始位置的参数控制着歌曲开始播放的地方。起始位置取决于音乐演奏的格式。MP3和OGG以时间为单位(以秒为单位)。MOD音乐是模式的序号。如果不能设置起始位置，通过一个startpos将会抛出一个NotImplementedError


time.sleep(10)

pygame.mixer.music.load('酒醉的蝴蝶.mp3')  #如果一个音乐流已经播放，它就会被停止。这并不是音乐的开始


while True:
    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()


    pygame.display.update()
复制代码
 

pygame.mixer.music.rewind() #重新启动音乐
#将当前音乐的播放重新设置为一开始
 

pygame.mixer.music.stop() #停止音乐播放
 

pygame.mixer.music.pause() #暂时停止音乐播放
pygame.mixer.music.unpause()   #恢复暂停音乐
 

pygame.mixer.music.fadeout(30000)  #再播放指定时间后就淡出并停止播放音乐
#单位：毫秒
#此函数将阻塞，直到音乐淡出
 

复制代码
print('音量0.5')
pygame.mixer.music.set_volume(0.5)  #调节音乐音量
#设置音乐播放的音量。值参数在0.0和1.0之间。当加载新音乐时，音量就会重置
time.sleep(30)
print('音量1')
pygame.mixer.music.set_volume(1)
time.sleep(30)
print('音量0.3')
pygame.mixer.music.set_volume(0.3)
复制代码
 

b=pygame.mixer.music.get_volume() #返回当前音量
#值将在0.0和1.0之间
 

b=pygame.mixer.music.get_busy()   #检查音乐流是否在播放
#当音乐流在积极播放时，就会返回True。当音乐空闲时，返回False
#暂停相当于在播放，返回True
 

复制代码
x=pygame.mixer.music.get_pos()  #获得音乐播放时间
#单位：毫秒
#注意：不是播放位置

pygame.mixer.music.set_pos(30)    #设定播放位置
'''
这将在播放播放的音乐文件中设置位置。“pos”的含义，一个浮点数(或一个可以转换为浮点数的数字)，取决于音乐的格式。对于MOD文件，它是模块中的整数模式号。从声音的开始，在几秒钟内，就会得到绝对的位置。对于MP3文件，它是相对位置，在几秒内，从当前位置。对于MP3文件中的绝对定位，首先调用rewind()。其他文件格式是不支持的。更新版本的sdl混音版本比以前更有定位支持。如果某个特定格式不支持定位，则会提高一个SDLError
【MP3：从当前位置再往后推延指定的秒数】
'''
复制代码
 

 

复制代码
import pygame,time

pygame.init()
screen = pygame.display.set_mode((196, 100))
pygame.display.set_caption("pygame.mouse函数")

pygame.mixer.music.load('酒醉的蝴蝶.mp3')
pygame.mixer.music.play()


pygame.mixer.music.set_endevent(pygame.KEYDOWN)   #当播放停止时，音乐会发送一个事件
#参数：事件
#每次音乐结束时，这个事件都会被排队，而不仅仅是第一次[只要不在播放状态，会一直发送]。为了防止事件被排队，请调用这个方法，没有参数

b=pygame.mixer.music.get_endevent()   #当播放停止时，获取set_endevent发送的事件--int
#pygame.KEYDOWN=2
#如果没有endevent，函数将返回pygame.NOEVENT

print('xxxxxxx',b)

while True:
    event=pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    print('aaaaaa',event)

    pygame.display.update()
复制代码
 

b=pygame.mixer.get_init()  #测试混音器是否初始化
#如果混音器已初始化，则返回正在使用的播放参数。如果混音器尚未初始化，则返回None
#get_init() -> (frequency, format, channels)
#(22050, -16, 2)




