import random


class Player:
    def __init__(self, name, hero):
        self.name = name
        self.hero = hero
        self.treasures = 0


def create_player(name, choice):
    if choice == 1:
        player = Player(name, knight)
        print(player.name, ", you are a Knight\nAttack: " + str( knight.attack) + "\nEndurance: " + str(
            knight.endurance) + "\nAgility: " + str(
            knight.agility) + "\nInitiative: " + str(
            knight.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif choice == 2:
        player = Player(name, mage)
        print(player.name, ", you are a Mage\nAttack: " + str(mage.attack) + "\nEndurance: " + str(mage.endurance) + "\nAgility: " + str(
                mage.agility) + "\nInitiative: " + str(
                mage.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
    elif choice == 3:
        player = Player(name, thief)
        print(player.name, ", you are a Thief\nAttack: " + str(thief.attack) + "\nEndurance: " + str(
            thief.endurance) + "\nAgility: " + str(
            thief.agility) + "\nInitiative: " + str(
            thief.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
    else:
        print("Invalid Choice")


class Knight:
    attack = int(6)
    endurance = int(9)
    agility = int(4)
    initiative = int(5)


class Mage:
    attack = int(9)
    endurance = int(4)
    agility = int(5)
    initiative = int(6)

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 80:
            return True
        else:
            return False


class Thief:
    attack = int(5)
    endurance = int(5)
    agility = int(7)
    initiative = int(7)

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 25:
            return True
        else:
            return False


class Empty:
    attack = int(0)
    endurance = int(0)
    agility = int(0)
    initiative = int(0)


knight = Knight()
mage = Mage()
thief = Thief()
