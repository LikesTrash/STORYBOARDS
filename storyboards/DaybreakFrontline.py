#STORYBOARDED USING frankhjwx's osu storyboard engine: https://github.com/frankhjwx/osu-storyboard-engine

from Storyboard.StoryboardManager import *
import random
import math

#DEFINE BEATMAP LOCATION
song_folder = 'C:\\Users\\David Jiang\\AppData\\Local\\osu!\\Songs\\949955 Kano - DAYBREAK FRONTLINE'
sb_filename = 'Kano - DAYBREAK FRONTLINE (ArcherSelwyn).osb'

#DEFINE FUNCTIONS
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
    #500 IS HOW MUCH PETALS TO GENERATE
    for i in range(500):
        objs.append(generateSakura(random.randint(0, 210000), 211800, random.randint(-122, 60), random.randint(-10,40)))
    return objs

# Create StoryboardManager
SBManager = StoryboardManager(song_folder, sb_filename, create_backup=True)

#ALIAS FUNCTIONS
skr = SakuraEffect()

SBManager.append_scene(skr)
SBManager.generate_storyboard(diff_specific=True)
SBManager.delete_backups()
