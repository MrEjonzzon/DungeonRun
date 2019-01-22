import room_class
import game


class Map:
    # Mapsize creator

    def __init__(self):
        self.mapcord = []
        self.curx = 0
        self.cury = 0
        self.prevroom = []
        self.demomap = []
        self.sizex = 0
        self.sizey = 0
        self.prevy = 0
        self.prevx = 0

    def mapsize(self, x, y):
        for r in range(x):
            for k in range(y):
                room = room_class.Room(r, k)
                self.mapcord.append(room)
        global sizex
        global sizey
        sizex = x
        sizey = y

    def map_choice(self):
        diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
        if diffpick == '1':
            self.mapsize(4, 4)
        elif diffpick == '2':
            self.mapsize(5, 5)
        elif diffpick == '3':
            self.mapsize(8, 8)


    # Set corner coodinates
        ne = 0, sizey-1
        sw = sizex-1, 0
        se = sizex-1, sizey-1

    # Start room selection
    def start_room(self):
        startroom = int(input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast\n'))
        if startroom == 1:
            curx = 0
            cury = 0
        elif startroom == 2:
            curx = sizex - 1
            cury = 0
        elif startroom == 3:
            curx = 0
            cury = sizey-1
        elif startroom == 4:
            curx = sizex - 1
            cury = sizey - 1

        else:
            print("Invalid selection")

    # Choose direction
    def moving(self):
        while True:
            direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east\n").lower()
            prevx = self.curx
            prevy = self.cury
            curx = self.curx
            cury = self.cury
            if direction == 'w':

                for newroom in self.mapcord:
                    if newroom.gety() == (cury - 1) and newroom.getx() == curx:
                        cury = (newroom.gety())
                        if newroom.getmon():
                            game.call_fight(newroom.monster_list)
                            break
                        else:
                            break
                        break
                if cury == prevy:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            elif direction == 's':
                for newroom in self.mapcord:
                    if newroom.gety() == (cury + 1) and newroom.getx() == curx:
                        cury = (newroom.gety())
                        if newroom.getmon():
                            game.call_fight(newroom.monster_list)
                            break
                        else:
                            break
                        break
                if cury == prevy:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            elif direction == 'a':

                for newroom in self.mapcord:
                    if newroom.getx() == (curx - 1) and newroom.gety() == cury:
                        curx = (newroom.getx())
                        if newroom.getmon():
                            game.call_fight(newroom.monster_list)
                            break
                        else:
                            break
                        break
                if curx == prevx:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            elif direction == 'd':

                for newroom in self.mapcord:
                    if newroom.getx() == (curx + 1) and newroom.gety() == cury:
                        curx = (newroom.getx())
                        if newroom.getmon():
                            game.call_fight(newroom.monster_list)
                            break
                        else:
                            break
                        break
                if curx == prevx:
                    print("You search the wall for a door but are unable to find one.")
                    continue
