import random


class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value


loose_coins = Treasure("Loose Coins", 2)
money_pouch = Treasure("Money Pouch", 6)
gold_jewelry = Treasure("Gold Jewelry", 10)
gemstone = Treasure("Gemstone", 14)
small_treasure_chest = Treasure("Small Treasure Chest", 20)


def random_generator():
    roll = (random.randint(1, 100))
    return roll


def loose_coins_rarity():
    if random_generator() <= 40:
        return True
    else:
        return False


def money_pouch_rarity():
    if random_generator() <= 20:
        return True
    else:
        return False


def gold_jewelry_rarity():
    if random_generator() <= 15:
        return True
    else:
        return False


def gemstone_rarity():
    if random_generator() <= 10:
        return True
    else:
        return False


def small_treasure_chest_rarity():
    if random_generator() <= 5:
        return True
    else:
        return False
