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



CR = CharacterRenderer(font_path='Fonts/togalite-medium.otf', file_path='SB/letters/')
# CR is a CharacterRenderer defined before
screentext = LyricParser(CR)
screentext.ass_reader('Subtitles\daybreakfinal.ass')
Sentences = screentext.get_sentences()
#now render
CR.render()

#Used in LyricsTime

def genLyric(sentence, posx, posy, start_t, end_t, scale=0.4):
    objs = []
    x = posx
    y = posy
    movespeed = 0.005
    for ch in sentence.letters:
        dt = random.randint(-200, 80)
        obj = Object(ch.filename, origin='BottomLeft')
        obj.Move(start_t - 300, end_t + 400, x, y, x + movespeed*(end_t-start_t+700), y)
        obj.Fade(start_t + dt - 100, start_t + dt + 400, 0, 1)
        obj.Fade(end_t + dt - 200, end_t + dt + 200, 1, 0)
        obj.Color(start_t, [255,255,255])
        obj.Scale(start_t, scale)
        x += (ch.width + spacing) * scale
        objs.append(obj)
    return objs


def lyricsTime(lp):
    objs = Scene()
    objs.append(genLyric(lp.sentences[0], 90, 400, 59, 2340))
    objs.append(genLyric(lp.sentences[1], 90, 400, 2342, 5670))
    objs.append(genLyric(lp.sentences[2], 90, 400, 5760, 9610))
    objs.append(genLyric(lp.sentences[3], 90, 400, 9670, 11910))
    objs.append(genLyric(lp.sentences[4], 90, 400, 11970, 13530))
    objs.append(genLyric(lp.sentences[5], 90, 400, 13640, 15100))
    objs.append(genLyric(lp.sentences[6], 90, 400, 15170, 16650))
    objs.append(genLyric(lp.sentences[7], 90, 400, 16720, 19210))
    objs.append(genLyric(lp.sentences[8], 90, 400, 19270, 21630))
    objs.append(genLyric(lp.sentences[9], 90, 400, 21700, 23960))
    objs.append(genLyric(lp.sentences[10], 90, 400, 24050, 26380))
    objs.append(genLyric(lp.sentences[11], 90, 400, 26440, 29480))
    objs.append(genLyric(lp.sentences[12], 90, 400, 29660, 31800))
    objs.append(genLyric(lp.sentences[13], 90, 400, 31910, 33450))
    objs.append(genLyric(lp.sentences[14], 90, 400, 33550, 35410))
    objs.append(genLyric(lp.sentences[15], 90, 400, 35420, 36090))
    objs.append(genLyric(lp.sentences[16], 90, 400, 36120, 37710))
    objs.append(genLyric(lp.sentences[17], 90, 400, 37740, 38690))
    objs.append(genLyric(lp.sentences[18], 90, 400, 38720, 40930))
    objs.append(genLyric(lp.sentences[19], 90, 400, 41040, 42040))
    objs.append(genLyric(lp.sentences[20], 90, 400, 42060, 45900))
    objs.append(genLyric(lp.sentences[21], 90, 400, 45930, 48300))
    objs.append(genLyric(lp.sentences[22], 90, 400, 48310, 50430))
    objs.append(genLyric(lp.sentences[23], 90, 400, 50500, 52650))
    objs.append(genLyric(lp.sentences[24], 90, 400, 52740, 55250))
    objs.append(genLyric(lp.sentences[25], 90, 400, 55290, 56250))
    objs.append(genLyric(lp.sentences[26], 90, 400, 56340, 58870))
    objs.append(genLyric(lp.sentences[27], 90, 400, 77750, 78930))
    objs.append(genLyric(lp.sentences[28], 90, 400, 79040, 82260))
    objs.append(genLyric(lp.sentences[29], 90, 400, 82570, 84040))




    return objs




screen = lyricsTime(screentext)



# Create StoryboardManager {
SBManager = StoryboardManager(song_folder, sb_filename, create_backup=True)

skr = SakuraEffect()

SBManager.append_scene(skr)
SBManager.append_scene(screen)

SBManager.generate_storyboard(diff_specific=True)
SBManager.delete_backups()
# }
