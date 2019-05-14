from Storyboard.StoryboardManager import *
from tools.LyricsParser import *
import random
import math

# math.pi also works
pi = 3.1415926
spacing = 0
song_folder = 'C:\\Users\\David Jiang\\AppData\\Local\\osu!\\Songs\\949955 Kano - DAYBREAK FRONTLINE'
sb_filename = 'Kano - DAYBREAK FRONTLINE (ArcherSelwyn).osb'

def generateSakura(start_t, end_t, start_x, start_y):
    sakura = Object('SB/sakura.png')
    x = start_x
    y = start_y
    scale = random.randint(10, 40) / 100
    xspeed = random.randint(5, 7)/180 / scale
    yspeed = random.randint(2, 4)/360 / scale
    xend = random.randint(-115, 780)
    yend = random.randint(70, 490)
    duration = (400 - y)/yspeed
    sakura.Move(start_t, start_t + duration, x, y, xend, yend)
    sakura.Scale(start_t, scale)
    sakura.Fade(start_t, start_t+500, 0, 1)
    sakura.Rotate(start_t, start_t + duration, random.random() * pi * 2, random.random() * pi * 4 + pi * 2)
    if start_t + duration > 211800:
        sakura.Fade(211790, 211800, 1, 0)
    return sakura

def SakuraEffect():
    objs = Scene()
    for i in range(500):
        objs.append(generateSakura(random.randint(0, 210000), 211800, random.randint(-122, 60), random.randint(-10,40)))
    return objs



CR = CharacterRenderer(font_path='Fonts/OKURIBITO.ttf', file_path='SB/let/')
# CR is a CharacterRenderer defined before
LP = LyricParser(CR)
LP.ass_reader('Subtitles\daybreakfinal.ass')
Sentences = LP.get_sentences()
#now render
CR.render()

#Used in LyricsTime

def genLyric(sentence, posx, posy, start_t, end_t, scale=0.6):
    objs = []
    x = posx
    y = posy
    movespeed = 0.005
    for ch in sentence.letters:
        dt = random.randint(-200, 200)
        obj = Object(ch.filename, origin='BottomLeft')
        obj.Move(start_t - 300, end_t + 400, x, y, x + movespeed*(end_t-start_t+700), y)
        obj.Fade(start_t + dt - 100, start_t + dt + 400, 0, 1)
        obj.Fade(end_t + dt - 200, end_t + dt + 200, 1, 0)
        obj.Color(start_t, [0,0,0])
        obj.Scale(start_t, scale)
        x += (ch.width + spacing) * scale
        objs.append(obj)
    return objs


def lyricsTime(lp):
    objs = Scene()
    objs.append(genLyric(lp.sentences[0], -35, 380, 59, 115173))
    return objs









# Create StoryboardManager {
SBManager = StoryboardManager(song_folder, sb_filename, create_backup=True)

skr = SakuraEffect()
lrt = lyricsTime

SBManager.append_scene(skr)
SBManager.append_scene(lrt)

SBManager.generate_storyboard(diff_specific=True)
SBManager.delete_backups()
# }
