import os
import pathlib

TOP_DIR = 'C:\\Users\\Erik\\Downloads\\profile-stale'

fs = []
for root, dirs, files in os.walk(TOP_DIR, topdown=False):
    for name in files:
        p = pathlib.Path(os.path.join(root, name))
        s = os.stat(p)
        ss = s.st_size
        if ss == 0:
            os.remove(p)
        else:
            fs.append(p)
    for name in dirs:
        p = pathlib.Path(os.path.join(root, name))
        if len(os.listdir(p)) == 0:
            print(f'removing {p}')
            os.rmdir(p)



q = 'hist'

strings = [str(x) for x in fs]

interesting = [x for x in fs if q in str(x).lower()]
# data = [os.stat(x) for x in interesting]

print()