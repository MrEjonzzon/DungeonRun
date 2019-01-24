import random
import battle
import monster
from save import GameState

class Player:
    def __init__(self, name, hero, previous_state):
        self.name = name
        self.hero = hero
        if previous_state:
            self.treasures = previous_state.list_of_treasures
        else:
            self.treasures = list()



def create_player(name, choice, previous_state):
    if choice == 1:
        knight = Knight()
        player = Player(name, knight, previous_state)
        print(player.name,", you are a Knight\nAttack: " + str(knight.attack) + "\nEndurance: " + str(
            knight.endurance) + "\nAgility: " + str(
            knight.agility) + "\nInitiative: " + str(
            knight.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif choice == 2:
        mage = Mage()
        player = Player(name, mage, previous_state)
        print(player.name,", you are a Mage\nAttack: " + str(mage.attack) + "\nEndurance: " + str(mage.endurance) + "\nAgility: " + str(
                mage.agility) + "\nInitiative: " + str(
                mage.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
    elif choice == 3:
        thief = Thief()
        player = Player(name, thief, previous_state)
        print(player.name,", you are a Thief\nAttack: " + str(thief.attack) + "\nEndurance: " + str(
            thief.endurance) + "\nAgility: " + str(
            thief.agility) + "\nInitiative: " + str(
            thief.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
    else:
        print("Invalid Choice")
    return player

class Knight:
    def __init__(self):
        self.name = "Knight"
        self.character = 1
        self.attack = 6
        self.endurance = 9
        self.agility = 4
        self.initiative = 5


class Mage:
    def __init__(self):
        self.name = "Mage"
        self.character = 2
        self.attack = 9
        self.endurance = 4
        self.agility = 5
        self.initiative = 6

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 80:
            return True
        else:
            return False


class Thief:
    def __init__(self):
        self.name = "Thief"
        self.character = 3
        self.attack = 5
        self.endurance = 5
        self.agility = 7
        self.initiative = 7

    def ability(self):
        chance = (random.randint(1, 100))
        if chance <= 25:
            return True
        else:
            return False


class Empty:
    def __init__(self):
        self.attack = 0
        self.endurance = 0
        self.agility = 0
        self.initiative = 0
