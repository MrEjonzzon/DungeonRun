import Creature
import Battle
import Ai
import Map
import random
'''from Save import GameState'''

def player_game():
    def player_info():
        option = int(input("Choose a name for new player or choose existing player: \n[1] New player \n[2] Existing Player \n"))
        if option == 1:
            print("pass1") # Test purpose, Delete later

        elif option == 2:# Test purpose, Delete later
            print("pass2")
        else:
            print("Invalid choice")
            player_info()
    #player_info()

    #game_state=GameState
    global choice
    choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
    global Hero
    if choice == 1:
        Hero = Creature.Knight
        print("You are a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif choice == 2:
        Hero = Creature.Mage
        print("You are a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
    elif choice == 3:
        Hero = Creature.Theif
        print("You are a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" +"\n\n")
    else:
        print("Invalid Choice")
    call_fight(True, False, True, True)

def call_fight(true_1, true_2, true_3, true_4):
    Battle.fight(true_1, true_2, true_3, true_4, Hero, choice)

def ai_game():
    hero_selection = int(input("What class should AI be?\n 1: Knight \n 2: Mage \n 3: Thief \n"))
    Ai.ai_class(hero_selection)
    Ai.ai_map_choice()
    Ai.ai_start_room()

def start_choice():
    while True:
        selection = int(input("Who is playing? \n[1] Player \n[2] AI\n"))
        if selection == 1:
            player_game()
        elif selection == 2:
            ai_game()
        else:
            print("Invalid Selection, try again\n")


start_choice()
