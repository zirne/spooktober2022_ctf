import string
import itertools

CHARS = string.ascii_letters
NUMS = string.digits
SPECIALS = "_-"

USABLE_CHARS = f'{CHARS}{NUMS}{SPECIALS}'

import itertools
d = set([''.join(x) for x in itertools.permutations([c for c in USABLE_CHARS], 3)])

def string_maker(strlen=1):
    return list(set([''.join(x) for x in itertools.permutations([c for c in USABLE_CHARS], strlen)]))
    retval = []
    print()



def creator(strlen=1):
    d = f'{CHARS}{NUMS}{SPECIALS}'
    retval = [c for c in d]
    while strlen > 0:
        if len(retval) == 0:
            retval = ''
        strlen = strlen - 1


    #return r
    print()


#creator(2)
r = string_maker(3)

# print()
if mai