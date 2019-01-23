import monster
import treasure


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.monster_list = []
        self.treasure_list = []
        self.monster_list.append(monster.giant_spider_rarity())
        self.monster_list.append(monster.skeleton_rarity())
        self.monster_list.append(monster.orc_rarity())
        self.monster_list.append(monster.troll_rarity())
        self.treasure_list.append(treasure.gemstone_rarity())
        self.treasure_list.append(treasure.money_pouch_rarity())
        self.treasure_list.append(treasure.gold_jewelry_rarity())
        self.treasure_list.append(treasure.loose_coins_rarity())
        self.treasure_list.append(treasure.small_treasure_chest_rarity())

    def getx(self):
        return self.x

    def gety(self):
        return self.y


class Map:
    # Mapsize creator
    def __init__(self):
        self.mapcord = []
        self.curx = 0
        self.cury = 0
        self.prevroom = []
        self.sizex = 0
        self.sizey = 0
        self.prevy = 0
        self.prevx = 0

    def mapsize(self, x, y):
        for r in range(x):
            for k in range(y):
                room = Room(r, k)
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
        else:
            print("Invalid selection")

        print()

    # Set corner coodinates
    '''
    ne = 0, sizey-1
    sw = sizex-1, 0
    se = sizex-1, sizey-1
    '''

    # Start room selection
    def start_room(self):
        startroom = int(input('Were would you like to start?\n[1] Northwest\n[2] Northeast\n[3] Southwest\n[4] Southeast\n'))
        if startroom == 1:
            self.curx = 0
            self.cury = 0
        elif startroom == 2:
            self.curx = sizex - 1
            self.cury = 0
        elif startroom == 3:
            self.curx = 0
            self.cury = sizey-1
        elif startroom == 4:
            self.curx = sizex - 1
            self.cury = sizey - 1

        else:
            print("Invalid selection")

    # Choose direction
    def moving(self):
        while True:
            print(self.cury, self.curx)
            direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east\n").lower()
            if direction == 'w':
                for newroom in self.mapcord:
                    if newroom.gety() == (self.cury - 1) and newroom.getx() == self.curx:
                        self.curx = self.prevx
                        self.cury = self.prevy
                        self.cury = (newroom.gety())
                        break
                if self.cury == self.prevy:
                    print("You search the wall for a door but are unable to find one.")
                    continue
            elif direction == 's':
                for newroom in self.mapcord:
                    if newroom.gety() == (self.cury + 1) and newroom.getx() == self.curx:
                        self.curx = self.prevx
                        self.cury = self.prevy
                        self.cury = (newroom.gety())
                        break
                if self.cury == self.prevy:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            elif direction == 'a':
                for newroom in self.mapcord:
                    if newroom.getx() == (self.curx - 1) and newroom.gety() == self.cury:
                        self.curx = (newroom.getx())
                        break
                if self.curx == self.prevx:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            elif direction == 'd':
                for newroom in self.mapcord:
                    if newroom.getx() == (self.curx + 1) and newroom.gety() == self.cury:
                        self.curx = (newroom.getx())
                        break
                if self.curx == self.prevx:
                    print("You search the wall for a door but are unable to find one.")
                    continue

            else:
                print("Invalid selection")
                continue
