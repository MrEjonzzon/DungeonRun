import random
# Treasure:
# Each room can have one, several or no treasures.
# Treasures would pick up Automatically when player enters room if there is no monsters in the room.
# If there is monster in the room the treasure would picked up unless the player get defeated by monsters or escaped from the room.
# Treasures are randomized in each room based on its usuality as shown in below chart.

#   #   #   #   #   #   #   #   #   #   #   #   #
# Treasure          	Value(Point)	Rarity  #
# Loose coins	          2	             40%    #
# Money pouch	          6	             20%    #
# Gold jewelry      	 10              15%    #
# Gemstone	             14              10%    #
# Small treasure chest	 20	              5%    #
#   #   #   #   #   #   #   #   #   #   #   #   #
class Treasure:

    def __init__(self, treasure_name, treasure_value, treasure_rarity):
        self.treasure_name = treasure_name
        self.treasure_value = treasure_value
        self.treasure_rarity = treasure_rarity


loose_coins = Treasure("loose_coins", 2, 40)
money_pouch = Treasure("money_pouch", 6, 20)
gold_jewelry = Treasure("gold_jewelry", 10, 15)
gemstone = Treasure("gemstone", 14, 10)
small_treasure_chest = Treasure("small_treasure_chest", 20, 5)

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

