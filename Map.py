import roomClass

map_coordinates = list()
current

# Mapsize creator

def mapsize(y, x):
    for r in range(y):

        for k in range(x):
            room = roomClass.Room(r, k)

            map_coordinates.insert(room.gety())

            map_coordinates.insert(room.getx())

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

print(mapcord)

# Set corner coodinates

ne = 0, sizey - 1

sw = sizex - 1, 0

se = sizex - 1, sizey - 1

# Start room selection

startroom = input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast')

if startroom == '1':

    currentcord.insert(0, 0)

elif startroom == '2':

    currentcord = ne

elif startroom == '3':

    currentcord = sw

elif startroom == '4':

    currentcord = se

print(currentcord)

# Choose direction

direction = input("Choose direction\n[W] to go north \n[A] to go west \n[S]To go south \n[D] to go east ").lower()
if direction == 'w':

    currentcord.insert([0], y)

    currentcord.insert([1], x)

    for room in mapcord:
        if (room.getx(-1) == currentcord[1]) and (y == currentcord[0]):
            currentcord = room.getx()
