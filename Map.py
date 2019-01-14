import roomClass
mapcord = []
curx = 0
cury = 0
prevroom = []

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


# Set corner coodinates
ne = 0, sizey-1
sw = sizex-1, 0
se = sizex-1, sizey-1


# Start room selection
startroom = input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast')
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

print(cury, curx)

# Choose direction
direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east").lower()
if direction == 'w':
    for newroom in mapcord:
        if newroom.gety() == (cury - 1) and newroom.getx() == curx:
            cury = (newroom.gety())
            break
elif direction == 's':
    for newroom in mapcord:
        if newroom.gety() == (cury + 1) and newroom.getx() == curx:
            cury = (newroom.gety())
            break
elif direction == 'a':
    for newroom in mapcord:
        if newroom.getx() == (curx - 1) and newroom.gety() == cury:
            curx = (newroom.getx())
            break
elif direction == 'd':
    for newroom in mapcord:
        if newroom.getx() == (curx + 1) and newroom.gety() == cury:
            curx = (newroom.getx())
            break

