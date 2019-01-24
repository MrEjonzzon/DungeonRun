import map
import player
import ai
import monster
import battle
import header


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
        name = input("What is your name? ")
        choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
        global character
        character = player.create_player(name, choice)
        Map.map_choice()
        Map.start_room()
        Map.exit_map(Map)
        walking(character)
        


    def choose_ai_class(self):
        name = input("What is the name of the AI? ")
        choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
        global ai
        ai = player.create_player(name, choice)
        ai_map.map_choice(ai)


    def start_choice(self):
        while True:
            selection = int(input("Who is playing? \n[1] Player \n[2] AI\n"))
            if selection == 1:
                self.player_info()
                break
            elif selection == 2:
                self.choose_ai_class()
                break


def main():
    header.Meny_DR()
    global Map
    global ai_map
    Map = map.Map()
    ai_map = ai.Map()
    g = Game()
    g.start_choice()

def walking(character):
    global game_battle
    game_battle = battle.Battle
    currentroom = None
    while True:
        direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east\n").lower()
        if direction == "w":
            currentroom = Map.move_north()

        elif direction == "s":
            currentroom = Map.move_south()

        elif direction == "a":
            currentroom = Map.move_west()

        elif direction == "d":
            currentroom = Map.move_east()

        if currentroom == "You search the wall for a door but are unable to find one.":
            print(currentroom)
            continue

        elif currentroom.exit:
            bye = input("Would you like to leave the map?\n[Y]es\n[N]o\n").lower()
            if bye == "y":
                print("Thank you for playing! BYE BYE")
                quit()
            else:
                continue

        else:
            # Put battle here
            print("Monsters")

            print(currentroom.monster_list)
            print(character.hero.character)

            if currentroom.monster_list[0]:
                game_battle.fight(game_battle, character, monster.create_giant_spider())

            if currentroom.monster_list[1]:
                game_battle.fight(game_battle, character, monster.create_skeleton())

            if currentroom.monster_list[2]:
                game_battle.fight(game_battle, character, monster.create_orc())

            if currentroom.monster_list[3]:
                game_battle.fight(game_battle, character, monster.create_troll())

            print("Treasures")

            print(currentroom.treasure_list)

            pass

if __name__ == "__main__":
    main()
