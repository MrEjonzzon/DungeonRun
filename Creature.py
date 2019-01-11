import random

class Mage():
    attack = int(9)
    endurance = int(4)
    agility = int(5)
    initiative = int(6)
    def ability(self):
        chance = (random.randint(1, 100))
        if chance < 80:
            return True
        else:
            return False

class Theif():
    attack = int(5)
    endurance = int(5)
    agility = int(7)
    initiative = int(7)
    def ability(self):
        chance = (random.randint(1, 100))
        if chance < 25:
            return True
        else:
            return False

class Knight():
    attack = int(6)
    endurance = int(9)
    agility = int(4)
    initiative = int(5)








