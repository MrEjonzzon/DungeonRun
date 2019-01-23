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
        player_map.map_choice()
        player_map.start_room()
        player_map.moving()

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

            elif selection == 2:
                self.choose_ai_class()
            else:
                print("Invalid Selection, try again\n")

def main():
    global player_map
    global ai_map
    player_map = map.Map()
    ai_map = ai.Map()
    g = Game()
    g.start_choice()


if __name__ == "__main__":
    main()
