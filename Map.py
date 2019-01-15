import roomClass
import random
#import Creature

mapcord = []

curx = 0
cury = 0

prevroom = []

prevy = 0
prevx = 0

sizex = 0
sizey = 0


# Mapsize creator
def mapsize(x, y):
    for r in range(x):
        for k in range(y):
            room = roomClass.Room(r, k)
            mapcord.append(room)
    global sizex
    global sizey
    sizex = x
    sizey = y


diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
if diffpick == '1':
    mapsize(4, 4)
elif diffpick == '2':
    mapsize(5, 5)
elif diffpick == '3':
    mapsize(8, 8)

number = len(mapcord)

'''
for i in number:
    Creature.troll_rarity()
    Creature.giant_spider()
    Creature.orc_rarity()
    Creature.skeleton_rarity()

# Set corner coodinates
ne = 0, sizey-1
sw = sizex-1, 0
se = sizex-1, sizey-1
'''

# Start room selection
startroom = input('\nWere would you like to start?\n\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast\n')
if startroom == '1':
    curx = 0
    cury = 0
elif startroom == '2':
    curx = sizex - 1
    cury = 0
elif startroom == '3':
    curx = 0
    cury = sizey-1
elif startroom == '4':
    curx = sizex - 1
    cury = sizey - 1

print("\nCurrent room : ", cury, ".", curx)

# Choose direction
direction = input("\nChoose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east").lower()
if direction == 'w':


    prevy = cury
    prevx = curx

    print("\nPrevious room :", prevy, ".", prevx, "\n")

    for newroom in mapcord:
        if newroom.gety() == (cury - 1) and newroom.getx() == curx:
            cury = (newroom.gety())

            break
elif direction == 's':

    prevy = cury
    prevx = curx

    print("\nPrevious room :", prevy, ".", prevx, "\n")



    for newroom in mapcord:
        if newroom.gety() == (cury + 1) and newroom.getx() == curx:
            cury = (newroom.gety())

            break
elif direction == 'a':



    prevy = cury
    prevx = curx

    print("\nPrevious room :", prevy, ".", prevx, "\n")

    for newroom in mapcord:
        if newroom.getx() == (curx - 1) and newroom.gety() == cury:
            curx = (newroom.getx())


            break
elif direction == 'd':

    prevy = cury
    prevx = curx

    print("\nPrevious room :", prevy, ".", prevx, "\n")

    for newroom in mapcord:
        if newroom.getx() == (curx + 1) and newroom.gety() == cury:
            curx = (newroom.getx())
            break

print("Current room : ", cury, ".", curx)

