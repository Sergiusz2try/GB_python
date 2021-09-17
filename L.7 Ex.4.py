import os

files = os.listdir()
size_dir = {}

list_100 = []
list_400 = []
list_800 = []
list_1000 = []

for file in files:
    size = os.stat(file).st_size
    if size <= 100:
        list_100.append(1)
    elif size <= 400:
        list_400.append(1)
    elif size <= 800:
        list_800.append(1)
    else:
        list_1000.append(1)

size_dir[100] = sum(list_100)
size_dir[400] = sum(list_400)
size_dir[800] = sum(list_800)
size_dir[1000] = sum(list_1000)

print(size_dir)
