import os, numpy
i = 0


file1 = open("C:\\Users\David Jiang\\Desktop\\osumapper-master\\osumapper-master\\v6.2\\maplist3.txt", "w")
path = "C:/Users/David Jiang/Desktop/osufiles"

files = os.listdir(path)
i = 1

for index, file in enumerate(files):
    file1.write(os.path.join(path, file))
    file1.writelines("\n")

file1.close()
