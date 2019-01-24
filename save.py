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


class GameStateManager:
    def load_all(self):
        try:
            with open('game_states.json') as game_states_json:
                game_states = json.load(game_states_json)
                return game_states
        except Exception as e:
            print("No previous player found ")
        return None


    def load(self, player_name):
        try:
            game_states = self.load_all()
            if not game_states:
                return None
            player_game_states = game_states.get(player_name, None)
            if player_game_states:
                game_state = GameState(player_name, player_game_states['hero'], player_game_states['treasures'])
                return game_state
        except Exception as e:
            print("No previous player found ")
        return None


    def save(self, game_state):
        """
        This method will create json file named game_state.json and open it on write mode
        :param game_states:
        :return:
        """
        try:
            game_state_data = self.load_all()
            if not game_state_data:
                game_state_data = dict()
            player_game_state = dict()
            player_game_state['hero'] = game_state.hero
            player_game_state['treasures'] = game_state.list_of_treasures
            game_state_data[game_state.player_name] = player_game_state
            with io.open ('game_states.json', 'w', encoding='utf8') as game_states_json_file:
                data = json.dumps(game_state_data, indent = 4, ensure_ascii=False)
                game_states_json_file.write(data)
        except Exception as e:
            print("The player you chose is exist, Enter the new name to continue or go one step back and choose within existing player: \n")
