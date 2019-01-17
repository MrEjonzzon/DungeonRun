import Creature
import Battle
import Map

def ai_class(selection):
    if selection == 1:
        Hero = Creature.Knight
        print("Ai is a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
    elif selection == 2:
        Hero = Creature.Mage
        print("Ai is a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability:  You have 80% chanse to escape" + "\n\n")
    elif selection == 3:
        Hero = Creature.Theif
        print("Ai is a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(
            Hero.endurance) + "\nAgility: " + str(
            Hero.agility) + "\nInitiative: " + str(
            Hero.initiative) + "\nSpecial ability: You have 25% chanse to dubble your damage" + "\n\n")
    else:
        print("Invalid selection")

def ai_map(size):
    if size == '1':
        Map.mapsize(4, 4)
    elif size == '2':
        Map.mapsize(5, 5)
    elif size == '3':
        Map.mapsize(8, 8)

