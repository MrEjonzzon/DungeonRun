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

    def ai_stuff(self):
        self.start_room()
        diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
        if diffpick == '1':
            self.mapsize(4, 4)
            self.move_easy()
        elif diffpick == '2':
            self.mapsize(5, 5)
            self.move_medium()
        elif diffpick == '3':
            self.mapsize(8, 8)
            self.move_hard()
        else:
            print("Invalid selection")

    # Set corner coodinates
        ne = 0, sizey-1
        sw = sizex-1, 0
        se = sizex-1, sizey-1

    # Start room selection
    def start_room(self):
        self.curx = 0
        self.cury = 0

    def right(self):
        prevx = self.curx
        prevy = self.cury
        curx = self.curx
        cury = self.cury
        for newroom in self.mapcord:
            if newroom.getx() == (curx + 1) and newroom.gety() == cury:
                curx = (newroom.getx())
                break
        if curx == prevx:
            print("You search the wall for a door but are unable to find one.")

    def left(self):
        prevx = self.curx
        prevy = self.cury
        curx = self.curx
        cury = self.cury
        for newroom in self.mapcord:
            if newroom.getx() == (curx - 1) and newroom.gety() == cury:
                curx = (newroom.getx())
                break
        if curx == prevx:
            print("You search the wall for a door but are unable to find one.")


    def down(self):
        prevx = self.curx
        prevy = self.cury
        curx = self.curx
        cury = self.cury
        print(cury, curx)
        for newroom in self.mapcord:
            if newroom.getx() == (curx + 1) and newroom.gety() == cury:
                curx = (newroom.getx())
                break
        if curx == prevx:
            print("You search the wall for a door but are unable to find one.")

    def move_easy(self):
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()

    def move_medium(self):
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()

    def move_hard(self):
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()
        self.down()
        self.right()
        self.down()
        self.left()

