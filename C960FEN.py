#Chess 960 position number to FEN script
#written by Jacob Arnold

import random
import pyperclip
import webbrowser

path = '/home/jacob/Chess/chess960-num-to-fen-script/C960STRT.TXT' #change this to the filepath you saved the C960STRT.TXT file in
lines = []

c = str(input('What would you like to do?  Press r for random position, press n to enter a position number: '))

if c == 'r':
    ran = random.randint(1, 960)

    with open(path) as f:
        for line in f:
            lines.append(line)
    o = (lines[ran])
    ou = o[36:89]

    print(ran)
    pyperclip.copy(ou)


elif c == 'n':
    i = int(input('enter chess960 position number: '))

    with open(path) as f:
        for line in f:
            lines.append(line)
        
    o = (lines[i])
    ou = o[36:89]

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


