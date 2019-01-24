import monster
import treasure
import ai_battle
import game

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
    global ai_battle
    ai_battle = ai_battle.Battle()
    global g
    g = game.Game()
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

    def map_choice(self, character):
        selection = int(input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n'))
        if selection == 1:
            self.mapsize(4, 4)
            self.moving(selection, character)
        elif selection == 2:
            self.mapsize(5, 5)
            self.moving(selection, character)
        elif selection == 3:
            self.mapsize(8, 8)
            self.moving(selection, character)
        else:
            print("Invalid selection")

    def start_room(self):
        self.curx = 0
        self.cury = 0

    def moving(self, selection, character):
        if selection == 1:
            self.move_easy(character)
        elif selection == 2:
            self.move_medium(character)
        elif selection == 3:
            self.move_hard(character)

    def move_south(self, character):
        for newroom in self.mapcord:
            if newroom.gety() == (self.cury + 1) and newroom.getx() == self.curx:
                self.prevy = self.curx
                self.prevy = self.cury
                self.cury = (newroom.gety())

                #Battle
                if newroom.monster_list[0]:
                    ai_battle.fight(character, monster.create_giant_spider())
                if newroom.monster_list[1]:
                    ai_battle.fight(character, monster.create_skeleton())
                if newroom.monster_list[2]:
                    ai_battle.fight(character, monster.create_orc())
                if newroom.monster_list[3]:
                    ai_battle.fight(character, monster.create_troll())
                    
                #Treasures
                if newroom.treasure_list[0]:
                    g.tot_treasure(character, treasure.loose_coins)
                    newroom.treasure_list[0] = map.set_false(newroom.treasure_list[0])
                if newroom.treasure_list[1]:
                    g.tot_treasure(character, treasure.money_pouch)
                    newroom.treasure_list[1] = map.set_false(newroom.treasure_list[1])
                if newroom.treasure_list[2]:
                    g.tot_treasure(character, treasure.gold_jewelry)
                    newroom.treasure_list[2] = map.set_false(newroom.treasure_list[2])
                if newroom.treasure_list[3]:
                    g.tot_treasure(character, treasure.gemstone)
                    newroom.treasure_list[3] = map.set_false(newroom.treasure_list[3])
                if newroom.treasure_list[4]:
                    g.tot_treasure(character, treasure.small_treasure_chest)
                    newroom.treasure_list[4] = map.set_false(newroom.treasure_list[4])

                print(self.cury, self.curx)
        return "You search the wall for a door but are unable to find one."

    def move_west(self, character):
        for newroom in self.mapcord:
            if newroom.getx() == (self.curx - 1) and newroom.gety() == self.cury:
                self.prevy = self.curx
                self.prevy = self.cury
                self.curx = (newroom.getx())

                #Battle
                if newroom.monster_list[0]:
                    ai_battle.fight(character, monster.create_giant_spider())
                if newroom.monster_list[1]:
                    ai_battle.fight(character, monster.create_skeleton())
                if newroom.monster_list[2]:
                    ai_battle.fight(character, monster.create_orc())
                if newroom.monster_list[3]:
                    ai_battle.fight(character, monster.create_troll())

                    # Treasures
                    if newroom.treasure_list[0]:
                        g.tot_treasure(character, treasure.loose_coins)
                        newroom.treasure_list[0] = map.set_false(newroom.treasure_list[0])
                    if newroom.treasure_list[1]:
                        g.tot_treasure(character, treasure.money_pouch)
                        newroom.treasure_list[1] = map.set_false(newroom.treasure_list[1])
                    if newroom.treasure_list[2]:
                        g.tot_treasure(character, treasure.gold_jewelry)
                        newroom.treasure_list[2] = map.set_false(newroom.treasure_list[2])
                    if newroom.treasure_list[3]:
                        g.tot_treasure(character, treasure.gemstone)
                        newroom.treasure_list[3] = map.set_false(newroom.treasure_list[3])
                    if newroom.treasure_list[4]:
                        g.tot_treasure(character, treasure.small_treasure_chest)
                        newroom.treasure_list[4] = map.set_false(newroom.treasure_list[4])

                print(self.cury, self.curx)
        return "You search the wall for a door but are unable to find one."

    def move_east(self, character):
        for newroom in self.mapcord:
            if newroom.getx() == (self.curx + 1) and newroom.gety() == self.cury:
                self.prevy = self.curx
                self.prevy = self.cury
                self.curx = (newroom.getx())

                #Battle
                if newroom.monster_list[0]:
                    ai_battle.fight(character, monster.create_giant_spider())
                if newroom.monster_list[1]:
                    ai_battle.fight(character, monster.create_skeleton())
                if newroom.monster_list[2]:
                    ai_battle.fight(character, monster.create_orc())
                if newroom.monster_list[3]:
                    ai_battle.fight(character, monster.create_troll())

                    # Treasures
                    if newroom.treasure_list[0]:
                        g.tot_treasure(character, treasure.loose_coins)
                        newroom.treasure_list[0] = map.set_false(newroom.treasure_list[0])
                    if newroom.treasure_list[1]:
                        g.tot_treasure(character, treasure.money_pouch)
                        newroom.treasure_list[1] = map.set_false(newroom.treasure_list[1])
                    if newroom.treasure_list[2]:
                        g.tot_treasure(character, treasure.gold_jewelry)
                        newroom.treasure_list[2] = map.set_false(newroom.treasure_list[2])
                    if newroom.treasure_list[3]:
                        g.tot_treasure(character, treasure.gemstone)
                        newroom.treasure_list[3] = map.set_false(newroom.treasure_list[3])
                    if newroom.treasure_list[4]:
                        g.tot_treasure(character, treasure.small_treasure_chest)
                        newroom.treasure_list[4] = map.set_false(newroom.treasure_list[4])

                print(self.cury, self.curx)

        return "You search the wall for a door but are unable to find one."


    def move_easy(self, character):
        # Move right X3
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down
        self.move_south(character)
        # Move left X3
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down
        self.move_south(character)
        # Move right X3
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down X1
        self.move_south(character)
        # Move left X3
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        print("Ai completed dungeon")

    def move_medium(self, character):
        # Move right X4
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down
        self.move_south(character)
        # Move left X4
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down
        self.move_south(character)
        # Move right X4
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down X1
        self.move_south(character)
        # Move left X4
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down X1
        self.move_south(character)
        # Move right X4
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        print("Ai completed dungeon")

    def move_hard(self, character):
        # Move right X7
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down
        self.move_south(character)
        # Move left X7
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down
        self.move_south(character)
        # Move right X7
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down X1
        self.move_south(character)
        # Move left X7
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down X1
        self.move_south(character)
        # Move right X7
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down X1
        self.move_south(character)
        # Move left X7
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        # Move down X1
        self.move_south(character)
        # Move right X7
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        self.move_east(character)
        # Move down X1
        self.move_south(character)
        # Move left X7
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        self.move_west(character)
        print("Ai completed dungeon")

