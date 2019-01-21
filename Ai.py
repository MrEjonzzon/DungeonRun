import Creature
import Battle
import Map
import random
import roomClass

def ai_class(selection):
    if selection == 1:
        Hero = Creature.Knight
        print("Ai is a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif selection == 2:
        Hero = Creature.Mage
        print("Ai is a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
    elif selection == 3:
        Hero = Creature.Theif
        print("Ai is a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
    else:
        print("Invalid selection")

def ai_start_room():
    Map.curx = 0
    Map.cury = 0



def ai_move_right():
    print(Map.cury, Map.curx)
    for room in Map.mapcord:
            Map.prevx = Map.curx
            Map.prevy = Map.cury
            for newroom in Map.mapcord:
                if newroom.getx() == (Map.curx + 1) and newroom.gety() == Map.cury:
                    Map.curx = (newroom.getx())
                    print(Map.cury, Map.curx)
def ai_move_left():
    print(Map.cury, Map.curx)
    for room in Map.mapcord:
        Map.prevx = Map.curx
        Map.prevy = Map.cury
        for newroom in Map.mapcord:
            if newroom.getx() == (Map.curx - 1) and newroom.gety() == Map.cury:
                Map.curx = (newroom.getx())
                print(Map.cury, Map.curx)


def ai_move_easy():
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()
    Map.cury += 1
    ai_move_left()

def ai_move_medium():
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()

def ai_move_hard():
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()
    Map.cury += 1
    ai_move_left()
    Map.cury += 1
    ai_move_right()
    Map.cury += 1
    ai_move_left()

def ai_map_choice():
    diffpick = input('Choose difficulty!\n[1] Easy\n[2] Medium\n[3] Hard\n')
    if diffpick == '1':
        Map.mapsize(4, 4)
        ai_start_room()
        ai_move_easy()
    elif diffpick == '2':
        Map.mapsize(5, 5)
        ai_start_room()
        ai_move_medium()
    elif diffpick == '3':
        Map.mapsize(8, 8)
        ai_start_room()
        ai_move_hard()







