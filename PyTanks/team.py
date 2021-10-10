import random

from PyTanks.player import Player
from PyTanks.utils import get_random_element_from_list


class Team:

    def __init__(self, name):
        self.name = name
        self.list_player = []

    def add_player(self, player):

        if player in self.list_player:
            raise ValueError('Player already team')

        if type(player).__name__ != 'Player':
            raise ValueError('Invalid player')

        self.list_player.append(player)

    def generate_players(self, team_size, tank_list):
        if team_size < 1 or team_size > 15:
            raise ValueError('invalid team size (1-15)')

        for i in range(1, team_size + 1):
            player_tank = get_random_element_from_list(tank_list)
            new_player = Player(player_tank)
            self.add_player(new_player)





