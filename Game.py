import Creature
import Battle

choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
if choice == 1:
    Hero = Creature.Knight
elif choice == 2:
    Hero = Creature.Mage
elif choice == 3:
    Hero = Creature.Theif
else:
    print("Invalid Choice")


current_health = Hero.endurance

current_health = Battle.attack_monster(4, Hero.agility, Hero.endurance)

print(current_health)









