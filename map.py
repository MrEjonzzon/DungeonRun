import monster
import treasure
import random


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
        self.exit = False

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
        self.prevy = 1
        self.prevx = 1

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
    def exit_map(self, map):
        door = random.choice(map.mapcord)
        print(door)
        print(len(self.mapcord))
        door.exit = True
        door.monster_list.clear()
        door.treasure_list.clear()

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

    def move_north(self):
        for newroom in self.mapcord:
            if newroom.gety() == (self.cury - 1) and newroom.getx() == self.curx:
                self.prevy = self.curx
                self.prevy = self.cury
                self.cury = (newroom.gety())
                return newroom
        return "You search the wall for a door but are unable to find one."

    def move_south(self):
        for newroom in self.mapcord:
            if newroom.gety() == (self.cury + 1) and newroom.getx() == self.curx:
                self.prevy = self.curx
                self.prevy = self.cury
                self.cury = (newroom.gety())
                return newroom
        return "You search the wall for a door but are unable to find one."

    def move_west(self):
        for newroom in self.mapcord:
            if newroom.getx() == (self.curx - 1) and newroom.gety() == self.cury:
                self.prevy = self.curx
                self.prevy = self.cury
                self.curx = (newroom.getx())
                return newroom
        return "You search the wall for a door but are unable to find one."

    def move_east(self):
        for newroom in self.mapcord:
            if newroom.getx() == (self.curx + 1) and newroom.gety() == self.cury:
                self.prevy = self.curx
                self.prevy = self.cury
                self.curx = (newroom.getx())
                return newroom
        return "You search the wall for a door but are unable to find one."