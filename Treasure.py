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

def loose_coins_rarity(roll):
    if (1 <= roll <= 40):
        print(roll)
        print("Loose coin treasure does exist")
    else:
        print(roll)
        print("Loose coin treasure does not exist")

def money_pouch_rarity(roll):
    if (1 <= roll <= 20):
        print(roll)
        print("Money pouch treasure does exist")
    else:
        print(roll)
        print("Money pouch treasure does not exist")

def gold_jewelry_rarity(roll):
    if (1 <= roll <= 15):
        print(roll)
        print("Gold jewelry treasure does exist")
    else:
        print(roll)
        print("Gold jewelry treasure does not exist")

def gemstone_rarity(roll):
    if(1 <= roll <= 10):
        print (roll)
        print ("Gemstone treasure does exist")
    else:
        print (roll)
        print ("Gemstone treasure does not exist")

def small_treasure_chest_rarity(roll):
    if (1 <= roll <= 5):
        print (roll)
        print ("Small treasure chest does exist")
    else:
        print (roll)
        print ("Small treasure chest does not exist")

loose_coins_rarity(random_generator())
money_pouch_rarity(random_generator())
gold_jewelry_rarity(random_generator())
gemstone_rarity(random_generator())
small_treasure_chest_rarity(random_generator())

