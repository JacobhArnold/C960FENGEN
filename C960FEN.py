#Chess 960 position number to FEN script
#written by Jacob Arnold

import random
import pyperclip
import webbrowser
import os
import sys

path = os.path.join(sys.path[0], 'C960STRT.TXT')
f = open(path)
lines = f.readlines()
f.close()


c = str(input('What would you like to do?  Press r for random position, press n to enter a position number: '))

if c == 'r':
    ran = random.randint(1, 960)
    ou = (lines[ran][36:89])
    print(ran)
    pyperclip.copy(ou)

elif c == 'n':
    i = int(input('enter chess960 position number: '))
    ou = (lines[i][36:89])
    pyperclip.copy(ou)

else:
    print('error: r/n not entered')


inp = str(input('do you want to open a lichess window? y/n:'))

if inp == 'y':
    out = 'https://lichess.org/analysis/chess960/' + ou
    webbrowser.open_new_tab(out)
    print(ou)

elif inp == 'n':
    print(ou)

else:
    print('error: y/n not entered')
