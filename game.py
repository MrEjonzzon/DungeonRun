import map
import player
import ai


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
        player.create_player(name, choice)
        Map.map_choice()
        Map.start_room()

    def choose_ai_class(self):
        name = input("What is the name of the AI? ")
        choice = int(input("Choose a hero \n 1: Knight \n 2: Mage \n 3: Thief \n"))
        player.create_player(name, choice)
        ai_map.ai_stuff()

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
    global Map
    global ai_map
    Map = map.Map()
    ai_map = ai.Map()
    g = Game()
    g.start_choice()
    while True:
        direction = input("Choose direction\n[W] to go north\n[A] to go west\n[S] to go south\n[D] to go east\n").lower()
        if direction == "w":
            currentroom = Map.move_north()
            if currentroom == "You search the wall for a door but are unable to find one.":
                print(currentroom)
                continue
            else:
                pass

        elif direction == "s":
            currentroom = Map.move_south()
            if currentroom == "You search the wall for a door but are unable to find one.":
                print(currentroom)
                continue
            else:
                pass

        elif direction == "a":
            currentroom = Map.move_west()
            if currentroom == "You search the wall for a door but are unable to find one.":
                print(currentroom)
                continue
            else:
                pass

        elif direction == "d":
            currentroom = Map.move_east()
            if currentroom == "You search the wall for a door but are unable to find one.":
                print(currentroom)
                continue
            else:
                pass


if __name__ == "__main__":
    main()
