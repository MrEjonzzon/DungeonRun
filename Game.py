import Creature

choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))

if choice == 1:
    Hero = Creature.Knight
elif choice == 2:
    Hero = Creature.Mage
elif choice == 3:
    Hero = Creature.Thief
else:
    print("Invalid Choice")

print(Hero.attack)






