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

    def fight(true_1, true_2, true_3, true_4):
        rounds = 1
        if true_1:
            monster_1 = Creature.giant_spider
            rounds = rounds + 1
        else:
            monster_1 = Creature.noone
        if true_2:
            monster_2 = Creature.skeleton
            rounds = rounds + 1
        else:
            monster_2 = Creature.noone
        if true_3:
            monster_3 = Creature.orc
            rounds = rounds + 1
        else:
            monster_3 = Creature.noone
        if true_4:
            monster_4 = Creature.troll
            rounds = rounds + 1
        else:
            monster_4 = Creature.noone

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
            while i < rounds:
                print("Hero hp:", current_health_hero)
                if true_1:
                    print(monster_1.name,"hp:", current_health_monster_1)
                if true_2:
                    print(monster_2.name,"hp:", current_health_monster_2)
                if true_3:
                    print(monster_3.name, "hp:", current_health_monster_3)
                if true_4:
                    print(monster_4.name, "hp:", current_health_monster_4)

                if hero_order >= monster_1_order and hero_order >= monster_2_order and hero_order >= monster_3_order and hero_order >= monster_4_order:
                    print("What monster do you want to attack?")
                    if true_1:
                        print("[1]", monster_1.name)
                    if true_2:
                        print("[2]", monster_2.name)
                    if true_3:
                        print("[3]", monster_3.name)
                    if true_4:
                        print("[4]", monster_4.name)
                    attack_who = int(input())

                    if attack_who == 1:
                        if true_1:
                            current_health_monster_1 = Battle.attack_hero(choice, Hero.attack, monster_1.agility, current_health_monster_1)
                        else:
                            print("Invalid Choice")
                    elif attack_who == 2:
                        if true_2:
                            current_health_monster_2 = Battle.attack_hero(choice, Hero.attack, monster_2.agility, current_health_monster_2)
                        else:
                            print("Invalid Choice")
                    elif attack_who == 3:
                        if true_3:
                            current_health_monster_3 = Battle.attack_hero(choice, Hero.attack, monster_3.agility, current_health_monster_3)
                        else:
                            print("Invalid Choice")
                    elif attack_who == 4:
                        if true_4:
                            current_health_monster_4 = Battle.attack_hero(choice, Hero.attack, monster_4.agility, current_health_monster_4)
                        else:
                            print("Invalid Choice")
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


    fight(True, False, False, True)

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
