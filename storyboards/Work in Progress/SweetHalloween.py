#STORYBOARDED USING frankhjwx's osu storyboard engine: https://github.com/frankhjwx/osu-storyboard-engine

from Storyboard.StoryboardManager import *
import random
import math

#DEFINE BEATMAP LOCATION
song_folder = 'C:\\Users\\David Jiang\\AppData\\Local\\osu!\\Songs\\968733 Yura_Hatsuki - Sweet Halloween'
sb_filename = 'Yura_Hatsuki - Sweet Halloween (W8TERM3LON).osb'

#MUSIC INFO
def musicInfo():
    objs = []

    blackBar1 = Object('STBD/CDBG.png', origin='TopCentre', x=320, y=0)
    blackBar1.Vector(0, '04:21:408', 854, 100)

    objs.append(blackBar1)

    return Scene(objs)

# Create StoryboardManager
SBManager = StoryboardManager(song_folder, sb_filename, create_backup=True)

#To alias Variables
musin = musicInfo()

SBManager.generate_storyboard(diff_specific=True)
SBManager.delete_backups()
