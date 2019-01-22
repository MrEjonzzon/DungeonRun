import map
import creature


def ai_class(selection):
    if selection == 1:
        Hero = creature.Knight
        print("Ai is a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif selection == 2:
        Hero = creature.Mage
        print("Ai is a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
    elif selection == 3:
        Hero = creature.Theif
        print("Ai is a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
    else:
        print("Invalid selection")

def ai_start_room():
    map.curx = 0
    map.cury = 0



def ai_move_right():
    print(map.cury, map.curx)
    for room in map.mapcord:
            map.prevx = map.curx
            map.prevy = map.cury
            for newroom in map.mapcord:
                if newroom.getx() == (map.curx + 1) and newroom.gety() == map.cury:
                    map.curx = (newroom.getx())
                    print(map.cury, map.curx)
def ai_move_left():
    print(map.cury, map.curx)
    for room in map.mapcord:
        map.prevx = map.curx
        map.prevy = map.cury
        for newroom in map.mapcord:
            if newroom.getx() == (map.curx - 1) and newroom.gety() == map.cury:
                map.curx = (newroom.getx())
                print(map.cury, map.curx)


def ai_move_easy():
    ai_move_right()
    map.cury += 1
    ai_move_left()
    map.cury += 1
    ai_move_right()
    map.cury += 1
    ai_move_left()

def ai_move_medium():
    ai_move_right()
    map.cury += 1
    ai_move_left()
    map.cury += 1
    ai_move_right()
    map.cury += 1
    ai_move_left()
    map.cury += 1
    ai_move_right()

def ai_move_hard():
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

def ai_map_choice():
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







