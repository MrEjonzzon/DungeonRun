import Creature
import Treasure

class Room:
    x = 0
    y = 0
    monster_list = []
    treasure_list = []
    monster_list.append(Creature.giant_spider_rarity())
    monster_list.append(Creature.skeleton_rarity())
    monster_list.append(Creature.orc_rarity())
    monster_list.append(Creature.troll_rarity())
    treasure_list.append(Treasure.gemstone_rarity())
    treasure_list.append(Treasure.gold_jewelry_rarity())
    treasure_list.append(Treasure.loose_coins_rarity())
    treasure_list.append(Treasure.small_treasure_chest_rarity())

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getx(self):
        return self.x

    def gety(self):
        return self.y

