import json
import io

class GameState:
    def __init__(self, player_name, hero, number_of_battles,treasures):#Score
        self.player_name = player_name
        self.hero = hero
        self.number_of_battles = number_of_battles
        self.treasures = treasures

    def __repr__(self):
        """
        Create a nice representation of this object, for debug purposes
        """
        return json.dumps(self.__dict__)




def save(game_state):
    #TODO


def load(player_name):
    #return game_state

def player_exists(player_name):
    #TODO
