import Creature
import Battle
import Ai
import Map
import random
'''from Save import GameState'''

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
            Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
    else:
        print("Invalid Choice")


def fight(monster_1, monster_2, monster_3, monster_4):

    knight_count = 0
    #order = Battle.fight_order(Hero.initiative, monster_1.initiative)
    current_health_hero = Hero.endurance
    current_health_monster_1 = monster_1.endurance
    current_health_monster_2 = monster_2.endurance
    current_health_monster_3 = monster_3.endurance
    current_health_monster_4 = monster_4.endurance
    hero_order1 = Battle.roll_dice(Hero.initiative)
    monster_1_order1 = Battle.roll_dice(monster_1.initiative)
    monster_2_order1 = Battle.roll_dice(monster_2.initiative)
    monster_3_order1 = Battle.roll_dice(monster_3.initiative)
    monster_4_order1 = Battle.roll_dice(monster_4.initiative)
    while (current_health_hero > 0) or (current_health_monster_1 > 0 and current_health_monster_2 > 0 and current_health_monster_3 > 0 and current_health_monster_4 > 0):
        hero_order = hero_order1
        monster_1_order = monster_1_order1
        monster_2_order = monster_2_order1
        monster_3_order = monster_3_order1
        monster_4_order = monster_4_order1

        i = 0
        while i < 5:
            print(" Hero hp:", current_health_hero, "\n", monster_1.name,"hp:", current_health_monster_1, "\n", monster_2.name,"hp:", current_health_monster_2,
                  "\n", monster_3.name, "hp:", current_health_monster_3, "\n", monster_4.name, "hp:", current_health_monster_4)

            if hero_order >= monster_1_order and hero_order >= monster_2_order and hero_order >= monster_3_order and hero_order >= monster_4_order:
                print("What monster do you want to attack?\n1:", monster_1.name, "\n2:", monster_2.name, "\n3:", monster_3.name, "\n4:", monster_4.name, "\n5: Run")
                attack_who = int(input())

                if attack_who == 1:
                    current_health_monster_1 = Battle.attack_hero(choice, Hero.attack, monster_1.agility, current_health_monster_1)
                elif attack_who == 2:
                    current_health_monster_2 = Battle.attack_hero(choice, Hero.attack, monster_2.agility, current_health_monster_2)
                elif attack_who == 3:
                    current_health_monster_3 = Battle.attack_hero(choice, Hero.attack, monster_3.agility, current_health_monster_3)
                elif attack_who == 4:
                    current_health_monster_4 = Battle.attack_hero(choice, Hero.attack, monster_4.agility, current_health_monster_4)
                elif attack_who == 5:
                    if Battle.escape(choice, Hero.agility):
                        break
                        print("hero escaped")
                i = i + 1
                hero_order = 0
            elif monster_1_order >= hero_order and monster_1_order >= monster_2_order and monster_1_order >= monster_3_order and monster_1_order >= monster_4_order:
                print("MONSTER 1 ATTACKS")
                current_health_hero = Battle.attack_monster(monster_1.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_1_order = 0
                knight_count = knight_count + 1
                i = i + 1


            elif monster_2_order >= monster_1_order and monster_2_order >= hero_order and monster_2_order >= monster_3_order and monster_2_order >= monster_4_order:
                print("MONSTER 2 ATTACKS")
                current_health_hero = Battle.attack_monster(monster_2.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_2_order = 0
                knight_count = knight_count + 1
                i = i + 1

            elif monster_3_order >= monster_1_order and monster_3_order >= monster_2_order and monster_3_order >= hero_order and monster_3_order >= monster_4_order:
                print("MONSTER 3 ATTACKS")
                current_health_hero = Battle.attack_monster(monster_3.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_3_order = 0
                knight_count = knight_count + 1
                i = i + 1

            elif monster_4_order >= monster_1_order and monster_4_order >= monster_2_order and monster_4_order >= monster_3_order and monster_4_order >= hero_order:
                print("MONSTER 4 ATTACKS")
                current_health_hero = Battle.attack_monster(monster_4.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_4_order = 0
                knight_count = knight_count + 1
                i = i + 1

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
            player_info()
            Map.map_choice()
            Map.start_room()
            Map.moving()

        elif selection == 2:
            ai_game()
        else:
            print("Invalid Selection, try again\n")


start_choice()
