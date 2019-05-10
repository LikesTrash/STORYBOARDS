import os
path = 'C:\\Users\\David Jiang\\Desktop\\osufiles'
files = os.listdir(path)
i = 1

for index, file in enumerate(files):
    os.rename(os.path.join(path, file), os.path.join(path, str(index)+'.osu'))
