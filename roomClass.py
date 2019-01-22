import Creature
import Treasure


class Room:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.monster_list = []
        self.treasure_list = []
        self.monster_list.append(Creature.giant_spider_rarity())
        self.monster_list.append(Creature.skeleton_rarity())
        self.monster_list.append(Creature.orc_rarity())
        self.monster_list.append(Creature.troll_rarity())
        self.treasure_list.append(Treasure.gemstone_rarity())
        self.treasure_list.append(Treasure.money_pouch_rarity())
        self.treasure_list.append(Treasure.gold_jewelry_rarity())
        self.treasure_list.append(Treasure.loose_coins_rarity())
        self.treasure_list.append(Treasure.small_treasure_chest_rarity())

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getmon(self):
        return self.monster_list
