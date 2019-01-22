import random
import Creature


def roll_dice(roll):
    result = int(0)
    i = 0
    while i < roll:
        dice = random.randint(1, 6)
        i = i+1
        result = result+dice
    return result


def fight_order(hero_initiative, monster_initiative):
    if roll_dice(hero_initiative) > roll_dice(monster_initiative):
        start = "hero"
        print("hero starts")
        return start
    else:
        print("monster starts")
        start = "monster"
        return start


def damage(health):
    new_health = health - 1
    return new_health


def attack_hero(thief, hero_attack, monster_agility, monster_health):
    hero_attack = roll_dice(hero_attack)
    monster_agility = roll_dice(monster_agility)
    if hero_attack > monster_agility:
        new_health = damage(monster_health)
        if thief == 3 and Creature.Theif.ability(False) == True:
            new_health = damage(new_health)
            print("thif hit double")
            return new_health
        else:
            print("hero hit")
            return new_health
    else:
        print("hero missed")
        return monster_health


def attack_monster(monster_attack, hero_agility, hero_health, knight, knight_count):
    monster_attack = roll_dice(monster_attack)

    hero_agility = roll_dice(hero_agility)
    if monster_attack > hero_agility:
        if knight == 1:
            if knight_count == 0:
                print("Knight blocked the attack")
                return hero_health
            else:
                new_health = damage(hero_health)
                print("monster hit")
                return new_health
        else:
            new_health = damage(hero_health)
            print("monster hit")
            return new_health
    else:
        print("monster missed")
        return hero_health


def escape(Mage, agility):
    if Mage == 2 and Creature.Mage.ability(False) == True:
        print("Mage fled the scene")
        return True
    elif Mage == 2 and Creature.Mage.ability(False) == False:
        print("Stay in room mage")
        return False
    else:
        chance = agility * 10
        flee = random.randint(1, 100)
        if flee < chance:
            print("Hero fled the scene")
            return True
        else:
            print("Stay in the room sir ")
            return False

def fight(true_1, true_2, true_3, true_4, Hero, choice):
    rounds = 1
    escape = False
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
    hero_order1 = roll_dice(Hero.initiative)
    monster_1_order1 = roll_dice(monster_1.initiative)
    monster_2_order1 = roll_dice(monster_2.initiative)
    monster_3_order1 = roll_dice(monster_3.initiative)
    monster_4_order1 = roll_dice(monster_4.initiative)
    while (current_health_hero > 0) or (current_health_monster_1 > 0 and current_health_monster_2 > 0 and current_health_monster_3 > 0 and current_health_monster_4 > 0) or escape == False:
        hero_order = hero_order1
        monster_1_order = monster_1_order1
        monster_2_order = monster_2_order1
        monster_3_order = monster_3_order1
        monster_4_order = monster_4_order1

        i = 0
        while i < rounds:
            print("Hero hp:", current_health_hero)
            if true_1:
                print(monster_1.name, "hp:", current_health_monster_1)
            if true_2:
                print(monster_2.name, "hp:", current_health_monster_2)
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
                print("[5] Run away")
                attack_who = int(input())

                if attack_who == 1:
                    if true_1:
                        current_health_monster_1 = attack_hero(choice, Hero.attack, monster_1.agility, current_health_monster_1)
                    else:
                        print("Invalid Choice")
                elif attack_who == 2:
                    if true_2:
                        current_health_monster_2 = attack_hero(choice, Hero.attack, monster_2.agility, current_health_monster_2)
                    else:
                        print("Invalid Choice")
                elif attack_who == 3:
                    if true_3:
                        current_health_monster_3 = attack_hero(choice, Hero.attack, monster_3.agility, current_health_monster_3)
                    else:
                        print("Invalid Choice")
                elif attack_who == 4:
                    if true_4:
                        current_health_monster_4 = attack_hero(choice, Hero.attack, monster_4.agility, current_health_monster_4)
                    else:
                        print("Invalid Choice")
                elif attack_who == 5:
                    if escape(choice, Hero.agility):
                        break
                        escape == True
                        print("hero escaped")
                i = i + 1
                hero_order = 0
            elif monster_1_order >= hero_order and monster_1_order >= monster_2_order and monster_1_order >= monster_3_order and monster_1_order >= monster_4_order:
                print("MONSTER 1 ATTACKS")
                current_health_hero = attack_monster(monster_1.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_1_order = 0
                knight_count = knight_count + 1
                i = i + 1


            elif monster_2_order >= monster_1_order and monster_2_order >= hero_order and monster_2_order >= monster_3_order and monster_2_order >= monster_4_order:
                print("MONSTER 2 ATTACKS")
                current_health_hero = attack_monster(monster_2.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_2_order = 0
                knight_count = knight_count + 1
                i = i + 1

            elif monster_3_order >= monster_1_order and monster_3_order >= monster_2_order and monster_3_order >= hero_order and monster_3_order >= monster_4_order:
                print("MONSTER 3 ATTACKS")
                current_health_hero = attack_monster(monster_3.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_3_order = 0
                knight_count = knight_count + 1
                i = i + 1

            elif monster_4_order >= monster_1_order and monster_4_order >= monster_2_order and monster_4_order >= monster_3_order and monster_4_order >= hero_order:
                print("MONSTER 4 ATTACKS")
                current_health_hero = attack_monster(monster_4.attack, Hero.agility, current_health_hero, choice, knight_count)
                monster_4_order = 0
                knight_count = knight_count + 1
                i = i + 1