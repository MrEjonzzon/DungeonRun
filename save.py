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
    game_states = dict()
    try:
        with open('game_states.json') as game_states_json:
            game_states = json.load(game_states_json)
    except Exception as e:
        print("No previous player found ")
    return game_states

def save(game_states):
    """
    This method will create json file named game_state.json and open it on write mode
    :param game_states:
    :return:
    """
    try:
        with io.open ('game_states.json', 'w', encoding='utf8') as game_states_json_file:
            data = json.dumps(game_states, indent = 4, ensure_ascii=False)
            game_states_json_file.write(data)
    except Exception as e:
        print("The player you chose is exist, Enter the new name to continue or go one step back and choose within existing player: \n")


def json_converter(obj):
   try:
      return obj.toJSON()
   except:
      return obj.__dict__


def get_validated_input(input_name, valid_inputs):
    in_value = input('Enter {}: '.format(input_name))
    if in_value not in valid_inputs:
        print('Invalid input, please enter one of valid choice: {}'.format(valid_inputs))
        in_value = get_validated_input(input_name, valid_inputs)
    return in_value


def player_identification():

    choice = None
    while choice != '4':
        print("Choose a name for new player or choose existing player: \n[1] New player \n[2] Show Existing Player list \n[3] Choose Existing player \n[4] Quit \n")
        choice = get_validated_input('operation', {'1', '2', '3', '4'})
        print('Processing operation {}'.format(choice))
        if choice != '4':
            game_states = load()
        if choice == '1':
            add_new_player(game_states)
        elif choice == '2':
            show_players_list(game_states)
        elif choice == '3':
            choose_player(game_states)
        if choice != '4':
            save(game_states)
    print('Happy gaming!')


def add_new_player(game_states):
    print('Adding new player')
    name = input('Please enter new player\'s name: ')
    new_player = New_player(name)
    game_states[name] = new_player

def show_players_list(game_state):
    print('Displaying players list')
    print(game_state)


def choose_player(game_states):
    print('Displaying list of players')
    name = input('Please enter name of existing player : ')
    try:
        print(game_states[name])
    except Exception as e:
        print('No player with name {} found'.format(name))

if __name__ == '__main__':
    begin_interaction()





def player_exists(player_name):
    # TODO complete this function
    pass
