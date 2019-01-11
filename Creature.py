class Monster:
    def __init__(self, name, initiative, endurance, attack, agility, rarity):
        self.name = name
        self.initiative = initiative
        self.endurance = endurance
        self.attack = attack
        self.agility = agility
        self.rarity = rarity

giant_spider = Monster("Giant Spider", 7, 1, 2, 3, 20)
skeleton = Monster("Skeleton", 4, 2, 3, 3, 15)
orc = Monster("Orc", 6, 3, 4, 4, 10)
troll = Monster("Troll", 2, 4, 7, 2, 5)


