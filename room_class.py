import creature
import treasure


class Room:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.monster_list = []
        self.treasure_list = []
        self.monster_list.append(creature.giant_spider_rarity())
        self.monster_list.append(creature.skeleton_rarity())
        self.monster_list.append(creature.orc_rarity())
        self.monster_list.append(creature.troll_rarity())
        self.treasure_list.append(treasure.gemstone_rarity())
        self.treasure_list.append(treasure.money_pouch_rarity())
        self.treasure_list.append(treasure.gold_jewelry_rarity())
        self.treasure_list.append(treasure.loose_coins_rarity())
        self.treasure_list.append(treasure.small_treasure_chest_rarity())

    def getx(self):
        return self.x

    def gety(self):
        return self.y

    def getmon(self):
        if len(self.monster_list) > 0:
            return True
