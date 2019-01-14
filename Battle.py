import random
import Game
import Creature

def roll_dice(roll):
        result = int(0)
        i = 0
        while i < roll:
            dice = random.randint(1, 6)
            i = i+1
            result = result+dice
        return result

def damage(loser):
    if loser == "monster":
        Game.monster.health = Game.monster.endurance-1
    elif loser == "Hero":
        Game.Hero.health = Game.Hero.endurance-1

def attack_hero():
    hero_attack = roll_dice(Game.Hero.attack)
    monster_agility = roll_dice(Game.monster.agility)
    if hero_attack > monster_agility:
        damage("monster")
    elif monster_agility > hero_attack:
        print("haha stupid human")

def attack_monster():
    monster_attack = roll_dice(Game.monster.attack)
    hero_agility = roll_dice(Game.Hero.agility)
    if monster_attack > hero_agility:
        damage("Hero")
    elif hero_agility > monster_attack:
        print("haha u missed")

def escape(Mage):
    if Mage == 2 and Creature.Mage.ability(False) == True:
        print("You are mage")
    else:
        chance = Game.Hero.agility * 10
        flee = random.randint(1, 100)
        if flee < chance:
            print("Hero fled the scene")
        else:
            print("Stay in the room sir ")





