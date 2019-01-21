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
    player_info()

    game_state=GameState

    choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
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

    def fight(monster_1, monster_2, monster_3, monster_4):
        knight_count = 0
        order = Battle.fight_order(Hero.initiative, monster_1.initiative)
        current_health_hero = Hero.endurance
        current_health_monster_1 = monster_1.endurance
        current_health_monster_2 = monster_2.endurance
        current_health_monster_3 = monster_3.endurance
        current_health_monster_4 = monster_4.endurance
        hero_order = Battle.roll_dice(Hero.initiative)
        print(hero_order)
        monster_1_order = Battle.roll_dice(monster_1.initiative)
        print(monster_1_order)
        monster_2_order = Battle.roll_dice(monster_2.initiative)
        print(monster_2_order)
        monster_3_order = Battle.roll_dice(monster_3.initiative)
        print(monster_3_order)
        monster_4_order = Battle.roll_dice(monster_4.initiative)
        print(monster_4_order)

        '''while True:
            print("hero hp:", current_health_hero)
            print("monster hp:", current_health_monster)
            if current_health_hero > 0 and current_health_monster > 0:
                if order == "hero":
                    battle_choice = int(input("1: Attack\n2: Escape\n"))
                    if battle_choice == 1:
                        current_health_monster = Battle.attack_hero(choice, Hero.attack, monster_1.agility, current_health_monster)
                        order = "monster"
                    elif battle_choice == 2:
                        if Battle.escape(choice, Hero.agility):
                            break
                        else:
                            order = "monster"
                elif order == "monster":
                    current_health_hero = Battle.attack_monster(monster_1.attack, Hero.agility, current_health_hero, choice, knight_count)
                    order = "hero"
                    knight_count = knight_count + 1
                else:
                    print("Invalid Choice")
            elif current_health_monster <= 0:
                print("monster died")
                break
            elif current_health_hero <= 0:
                print("you died")
                break'''


    fight(Creature.skeleton, Creature.troll, Creature.giant_spider, Creature.orc)

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
