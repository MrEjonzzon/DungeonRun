import map
import creature


class Ai:

    def __init__(self, attack, endurance, agility, initiative, hero):
        self.attack = attack
        self.endurance = endurance
        self.agility = agility
        self.initiative = initiative
        self.hero = hero

    def ai_class(self, selection):
        if selection == 1:
            self.hero = creature.Knight
            print("Ai is a knight\nAttack: " + str(self.hero.attack) + "\nEndurance: "
                  + str(self.hero.endurance)+ "\nAgility: "
                  + str(self.hero.agility) + "\nInitiative: "
                  + str(self.hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
        elif selection == 2:
            self.hero = creature.Mage
            print("Ai is a mage\nAttack: " + str(self.hero.attack) + "\nEndurance: " + str(
                self.hero.endurance) + "\nAgility: " + str(
                self.hero.agility) + "\nInitiative: " + str(
                self.hero.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
        elif selection == 3:
            self.hero = creature.Theif
            print("Ai is a theif\nAttack: " + str(self.hero.attack) + "\nEndurance: " + str(
                self.hero.endurance) + "\nAgility: " + str(
                self.hero.agility) + "\nInitiative: " + str(
                self.hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
        else:
            print("Invalid selection")

    def ai_start_room(self):
        map.curx = 0
        map.cury = 0



    def ai_move_right(self):
        print(map.cury, map.curx)
        for room in map.mapcord:
                map.prevx = map.curx
                map.prevy = map.cury
                for newroom in map.mapcord:
                    if newroom.getx() == (map.curx + 1) and newroom.gety() == map.cury:
                        map.curx = (newroom.getx())
                        print(map.cury, map.curx)
    def ai_move_left(self):
        print(map.cury, map.curx)
        for room in map.mapcord:
            map.prevx = map.curx
            map.prevy = map.cury
            for newroom in map.mapcord:
                if newroom.getx() == (map.curx - 1) and newroom.gety() == map.cury:
                    map.curx = (newroom.getx())
                    print(map.cury, map.curx)


    def ai_move_easy(self):
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()
        map.cury += 1
        ai_move_left()

    def ai_move_medium(self):
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()

    def ai_move_hard(self):
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()
        map.cury += 1
        ai_move_left()
        map.cury += 1
        ai_move_right()
        map.cury += 1
        ai_move_left()

    def ai_map_choice(self):
        diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
        if diffpick == '1':
            map.mapsize(4, 4)
            ai_start_room()
            ai_move_easy()
        elif diffpick == '2':
            map.mapsize(5, 5)
            ai_start_room()
            ai_move_medium()
        elif diffpick == '3':
            map.mapsize(8, 8)
            ai_start_room()
            ai_move_hard()












