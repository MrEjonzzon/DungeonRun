import Creature
import Battle

choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
if choice == 1:
    Hero = Creature.Knight
    print("You are a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
        Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
elif choice == 2:
    Hero = Creature.Mage
    print("You are a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
        Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability:  You have 80% chanse to escape" + "\n\n")
elif choice == 3:
    Hero = Creature.Theif
    print("You are a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
        Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You have 25% chanse to dubble your damage" +"\n\n")
else:
    print("Invalid Choice")

def fight(monster):
    order = Battle.fight_order(Hero.initiative, monster.initiative)
    current_health_hero = Hero.endurance
    current_health_monster = monster.endurance
    knight_count = 0
    while True:
        print("hero hp:", current_health_hero)
        print("monster hp:", current_health_monster)
        if current_health_hero > 0 and current_health_monster > 0:
            if order == "hero":
                battle_choice = int(input("1: Attack\n2: Escape\n"))
                if battle_choice == 1:
                    current_health_monster = Battle.attack_hero(choice, Hero.attack, monster.agility, current_health_monster)
                    order = "monster"
                elif battle_choice == 2:
                    if Battle.escape(choice, Hero.agility):
                        break
                    else:
                        order = "monster"
            elif order == "monster":
                current_health_hero = Battle.attack_monster(monster.attack, Hero.agility, current_health_hero, choice, knight_count)
                order = "hero"
                knight_count = knight_count + 1
            else:
                print("Invalid Choice")
        elif current_health_monster <= 0:
            print("monster died")
            break
        elif current_health_hero <= 0:
            print("you died")
            break


fight(Creature.skeleton)

