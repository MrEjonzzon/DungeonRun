import random
# Treasure:
# Each room can have one, several or no treasures.
# Treasures would pick up Automatically when player enters room if there is no monsters in the room.
# If there is monster in the room the treasure would picked up unless the player get defeated by monsters or escaped from the room.
# Treasures are randomized in each room based on its usuality as shown in below chart.

#   #   #   #   #   #   #   #
# Treasure          	Value(Point)	Rarity
# Loose coins	          2	             40%
# Money pouch	          6	             20%
# Gold jewelry      	 10              15%
# Gemstone	             14              10%
# Small treasure chest	 20	              5%

class Treasure:

    def __init__(self, treasure_name, treasure_value, treasure_rarity):
        self.treasure_name = treasure_name
        self.treasure_value = treasure_value
        self.treasure_rarity = treasure_rarity




loose_coins = Treasure("loose_coins", 2, 40)
money_pouch = Treasure("money_pouch", 6, 20)
gold_jewelery = Treasure("gold_jewelery", 10, 15)
gemstone = Treasure("gemstone", 14, 10)
small_treasure_chest = Treasure("small_treasure_chest", 20, 5)

def loose_coins_rarity():
     roll = random.randint(1,100)
if (loose_coins_rarity.roll >= 1 and loose_coins_rarity.roll<= 40):
    put in map
else:
    dont put in map


def money_pouch_rarity():
     roll = random.randint(1,100)
if (money_pouch_rarity.roll >= 1 and money_pouch_rarity.roll<= 20):
    put in map
else:
    dont put in map

    def gold_jewelery_rarity():
     roll = random.randint(1,100)
if (gold_jewelery_rarity.roll >= 1 and gold_jewelery_rarity.roll<= 15):
    put in map
else:
    dont put in map

    def gemstone_rarity():
     roll = random.randint(1,100)
if (gemstone_rarity.roll >= 1 and gemstone_rarity.roll<= 10):
    put in map
else:
    dont put in map

    def small_treasure_chest_rarity():
     roll = random.randint(1,100)
if (small_treasure_chest_rarity.roll >= 1 and small_treasure_chest_rarity.roll<= 5):
    put in map
else:
    dont put in map
