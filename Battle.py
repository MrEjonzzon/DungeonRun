import random

import Game


def roll_dice(roll):
        result=int(0)

        i = 0
        while i < roll:
            dice = random.randint(1, 6)

            i=i+1
            result=result+dice
        return result




def damage(loser):
    result= 0

    i = 0
    if loser == "monster":
        Game.monster.health=Game.monster.health-1

    elif loser == "Hero":
        Game.hero.health=Game.hero.health-1


def attack_hero():

    hero_attack = roll_dice(Game.hero.attack)
    monster_agility= roll_dice(Game.monster.agility)

    if hero_attack > monster_agility:
       damage("monster")

    elif monster_agility > hero_attack:
        print("haha stupid human")


def attack_monster():

    monster_attack = roll_dice(Game.monster.attack)
    hero_agility = roll_dice(Game.hero.agility)

    if monster_attack > hero_agility:
        damage("Hero")

    elif hero_agility > monster_attack:
        print("haha u missed")




def escape():

    chance = Game.hero.agility * 10
    flee = random.randint(1, 100)
    if flee < chance:
        print("Hero fled the scene")
    else:
        print("Stay in the room sir ")






