import map
import player
import ai
import monster
import battle
import header
import treasure
import save


class Game:
    def player_info(self):
        option = int(input("Choose a name for new player or choose existing player: \n[1] New player\n[2] Existing Player\n[3] Show Highscore\n[4] Quit\n"))
        if option == 1:
            self.Choose_class()
        elif option == 2:  # Test purpose, Delete later
            print("pass2")
        elif option == 3:
            pass    # Highscore list
        elif option == 4:
            header.Bye_bye()
            quit()
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

    def tot_treasure(self, character, treasure_value):
        character.treasures += treasure_value.value

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
    g = Game()

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

        if currentroom == "You search the wall for a door but are unable to find one\n":
            print(currentroom)
            continue

        elif currentroom.exit:
            bye = input("Would you like to leave the map?\n[Y]es\n[N]o\n").lower()
            if bye == "y":
                print("Thank you for playing! BYE BYE")
                #Put save here
                save.save_game(character.name, character.hero.name, character.treasures)
                main()
            else:
                continue

        else:
            got_treasure = False
            # Put battle here
            fight = True
            while fight:
                if currentroom.monster_list[0]:
                    fight = game_battle.fight(game_battle, character, monster.create_giant_spider())
                    if fight:
                        currentroom.monster_list[0] = map.set_false(currentroom.monster_list[0])
                    elif fight == None:
                        header.Bye_bye()
                        quit()
                elif currentroom.monster_list[1]:
                    fight = game_battle.fight(game_battle, character, monster.create_skeleton())
                    if fight:
                        currentroom.monster_list[1] = map.set_false(currentroom.monster_list[1])
                    elif fight == None:
                        header.Bye_bye()
                        quit()
                elif currentroom.monster_list[2]:
                    fight = game_battle.fight(game_battle, character, monster.create_orc())
                    if fight:
                        currentroom.monster_list[2] = map.set_false(currentroom.monster_list[2])
                    elif fight == None:
                        header.Bye_bye()
                        quit()
                elif currentroom.monster_list[3]:
                    fight = game_battle.fight(game_battle, character, monster.create_troll())
                    if fight:
                        currentroom.monster_list[3] = map.set_false(currentroom.monster_list[3])
                    elif fight == None:
                        header.Bye_bye()
                        quit()
                else:
                    print("Room has no monsters")
                    fight = False
                    if currentroom.treasure_list[0]:
                        g.tot_treasure(character, treasure.loose_coins)
                        print("You found some", treasure.loose_coins.name, "!\nWorth: 2 points\n")
                        got_treasure = True

                    if currentroom.treasure_list[1]:
                        g.tot_treasure(character, treasure.money_pouch)
                        print("You found a", treasure.money_pouch.name, "!\nWorth: 6 points\n")
                        got_treasure = True

                    if currentroom.treasure_list[2]:
                        g.tot_treasure(character, treasure.gold_jewelry)
                        print("You found", treasure.gold_jewelry.name, "!\nWorth: 10 points\n")
                        got_treasure = True

                    if currentroom.treasure_list[3]:
                        g.tot_treasure(character, treasure.gemstone)
                        print("You found a", treasure.gemstone.name, "!\nWorth: 14 points\n")
                        got_treasure = True

                    if currentroom.treasure_list[4]:
                        g.tot_treasure(character, treasure.small_treasure_chest)
                        print("You found a", treasure.small_treasure_chest.name, "!\nWorth: 20 points\n")
                        got_treasure = True

                    if got_treasure:
                        print("Your bag is filled with new treasure!\nYou treasure is now worth\n", character.treasures)
                        currentroom.treasure_list[0] = map.set_false(currentroom.treasure_list[0])
                        currentroom.treasure_list[1] = map.set_false(currentroom.treasure_list[1])
                        currentroom.treasure_list[2] = map.set_false(currentroom.treasure_list[2])
                        currentroom.treasure_list[3] = map.set_false(currentroom.treasure_list[3])
                        currentroom.treasure_list[4] = map.set_false(currentroom.treasure_list[4])

def main():
    header.Meny_DR()
    global Map
    global ai_map
    Map = map.Map()
    ai_map = ai.Map()
    g = Game()
    g.start_choice()

if __name__ == "__main__":
    main()
