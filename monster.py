import random


class Monster:
    def __init__(self, name, initiative, endurance, attack, agility):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility


class Giant_Spider:
    def __init__(self):
        self.name = "Giant Spider"
        self.initiative = 7
        self.endurance = 1
        self.attack = 2
        self.agility = 3


class Skeleton:
    def __init__(self):
        self.name = "Skeleton"
        self.initiative = 4
        self.endurance = 2
        self.attack = 3
        self.agility = 3


class Orc:
    def __init__(self):
        self.name = "Orc"
        self.initiative = 6
        self.endurance = 3
        self.attack = 4
        self.agility = 4


class Troll:
    def __init__(self):
        self.name = "Troll"
        self.initiative = 2
        self.endurance = 4
        self.attack = 7
        self.agility = 2


def create_giant_spider():
    giant_spider = Giant_Spider()
    return giant_spider


def create_skeleton():
    skeleton = Skeleton()
    return skeleton


def create_orc():
    orc = Orc()
    return orc


def create_troll():
    troll = Troll()
    return troll


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




