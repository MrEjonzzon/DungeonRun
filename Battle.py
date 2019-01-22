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
