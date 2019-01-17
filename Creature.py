import random


class Mage:
    attack = int(9)
    endurance = int(4)
    agility = int(5)
    initiative = int(6)

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 80:
            return True
        else:
            return False


class Theif:
    attack = int(5)
    endurance = int(5)
    agility = int(7)
    initiative = int(7)

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 25:
            return True
        else:
            return False


class Knight:
    attack = int(6)
    endurance = int(9)
    agility = int(4)
    initiative = int(5)


class Monster:
    def __init__(self, name, initiative, endurance, attack, agility):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility


giant_spider = Monster("Giant Spider", 7, 1, 2, 3)
skeleton = Monster("Skeleton", 4, 2, 3, 3)
orc = Monster("Orc", 6, 3, 4, 4)
troll = Monster("Troll", 2, 4, 7, 2)



def random_generator():
    roll = (random.randint(1, 100))
    return roll


def giant_spider_rarity():
    if random_generator() <= 20:
        return True
    else:
        return False


def skeleton_rarity():
    if random_generator() <= 15:
        return True
    else:
        return False


def orc_rarity():
    if random_generator() <= 10:
        return True
    else:
        return False


def troll_rarity():
    if random_generator() <= 5:
        return True
    else:
        return False
