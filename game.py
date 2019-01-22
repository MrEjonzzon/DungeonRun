import map
import creature
import ai
import battle

'''from Save import GameState'''


class Game:
    def player_info(self):
        option = int(input("Choose a name for new player or choose existing player: \n[1] New player \n[2] Existing Player \n"))
        if option == 1:
            print("pass1")  # Test purpose, Delete later
            self.Choose_class()
        elif option == 2:  # Test purpose, Delete later
            print("pass2")
        else:
            print("Invalid choice")

    def Choose_class(self):
        global choice
        choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
        global Hero
        if choice == 1:
            Hero = creature.Knight
            print("You are a knight\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
                Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You block the first hit from a monster" + "\n\n")
        elif choice == 2:
            Hero = creature.Mage
            print("You are a mage\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
                Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability:  You have 80% chance to escape" + "\n\n")
        elif choice == 3:
            Hero = creature.Theif
            print("You are a theif\nAttack: " + str(Hero.attack) + "\nEndurance: " + str(Hero.endurance) + "\nAgility: " + str(
                Hero.agility) + "\nInitiative: " + str(Hero.initiative) + "\nSpecial ability: You have 25% chance to double your damage" + "\n\n")
        else:
            print("Invalid Choice")

        mymap.map_choice()
        mymap.start_room()
        mymap.moving()

    def call_fight(self, monster_list):
        battle.fight(monster_list, Hero, choice)

    def ai_game(self):
        hero_selection = int(input("What class should AI be?\n 1: Knight \n 2: Mage \n 3: Thief \n"))
        sada = ai.Ai(1, 2, 34, 4, creature.Knight)
        sada.ai_class(hero_selection)
        sada.ai_map_choice()
        sada.ai_start_room()

    def start_choice(self):
        while True:
            selection = int(input("Who is playing? \n[1] Player \n[2] AI\n"))
            if selection == 1:
                self.player_info()

            elif selection == 2:
                self.ai_game()
            else:
                print("Invalid Selection, try again\n")


def main():
    global mymap
    mymap = map.Map()
    g = Game()
    Game.start_choice(g)
    sada = ai.Ai(1, 2, 34, 4, creature.Knight)
    sada.ai_class(hero_selection)
    


if __name__ == "__main__":
    main()
