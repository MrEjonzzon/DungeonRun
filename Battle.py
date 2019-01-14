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
    health = health - 1
    return health

def attack_hero(thief, hero_attack, monster_agility, monster_health):
    hero_attack = roll_dice(hero_attack)
    monster_agility = roll_dice(monster_agility)
    if thief == 3 and Creature.Theif.ability(False) == True:
        hero_attack = hero_attack * 2

    if hero_attack > monster_agility:
        new_health = damage(monster_health)
        return new_health
    elif monster_agility > hero_attack:
        print("haha stupid human")

def attack_monster(monster_attack, hero_agility, hero_health):
    monster_attack = roll_dice(monster_attack)
    hero_agility = roll_dice(hero_agility)
    if monster_attack > hero_agility:
        new_health = damage(hero_health)
        return new_health
    elif hero_agility > monster_attack:
        print("haha u missed")

def escape(Mage, agility):
    if Mage == 2 and Creature.Mage.ability(False) == True:
        print("You are mage")
    elif Mage == 2 and Creature.Mage.ability(False) == False:
        print("Stay in room mage")
    else:
        chance = agility * 10
        flee = random.randint(1, 100)
        if flee < chance:
            print("Hero fled the scene")
        else:
            print("Stay in the room sir ")





