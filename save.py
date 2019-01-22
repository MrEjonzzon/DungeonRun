import json
import io

class GameState:
    def __init__(self, player_name, hero, list_of_treasures):
        """
        Create constructor of game state with respective data
        """
        self.player_name = player_name
        self.hero = hero
        self.list_of_treasures = list_of_treasures

    def __repr__(self):
        """
        Create a  representation of this object, for debug purposes
        """
        return json.dumps(self.__dict__)


def load():
    try:
        with open('game_state.json') as game_state_json:
            game_state = json.load(game_state_json)
            return game_state
    except Exception as e:
        print("No previous player found ")


def save(game_state):
    """
    This method will create json file named game_state.json and open it on write mode
    :param game_state:
    :return:
    """
    try:
        with io.open ('game_state.json', 'w', encoding='utf8') as game_state_json_file:
            data = json.dumps(game_state, indent = 4, ensure_ascii=False)
            game_state_json_file.write(data)
    except Exception as e:
        print("The player you chose is exist, Enter the new name to continue or go one step back and choose within existing player: \n")


def player_exists(player_name):
    # TODO complete this function
    pass
