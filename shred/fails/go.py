import pathlib
import os
import fs
IMG_PATH = "fat://C:\\Users\\Erik\\PycharmProjects\\spooktober_ctf\\shred\\usb-backup.img"
OUTPUT_PATH = '.'

os.makedirs(OUTPUT_PATH, exist_ok=True)

#with fs.open_fs(IMG_PATH) as my_fs:
#    my_fs.open('Recept kycklingpasta.pdf', mode='rb')



my_fs = fs.open_fs("fat://C:\\Users\\Erik\\PycharmProjects\\spooktober_ctf\\shred\\usb-backup.img")

#asd = my_fs.tree()

files = [path for path in my_fs.walk.files()]

for path in files:
    data = my_fs.open(path, mode='rb').read()
    path_to_target = pathlib.Path(OUTPUT_PATH, pathlib.Path(path).name)
    with open(path_to_target, mode='wb') as h:
        h.write(data)
    #print(f'{data}')

print()