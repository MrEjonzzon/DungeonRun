import Creature


class Room:
    global roomMonster
    roomMonster = []
    treasure = []
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        if Creature.giant_spider_rarity():
            Spider = Creature.Monster("Giant Spider", 7, 1, 2, 3)
            roomMonster.append(Spider)

    def getx(self):
        return self.x

    def gety(self):
        return self.y
