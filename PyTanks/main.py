from copy import copy

from PyTanks.base_tank import BaseTank
from PyTanks.player import Player
from PyTanks.team import Team
from PyTanks.enum_tank_type import TankType
from PyTanks.wot_api import WotAPI

if __name__ == '__main__':

    wot_api = WotAPI()
    tank_list = wot_api.get_tank_list(1)
    print(tank_list)

    # team_beacon = Team('Beacon')
    # team_slavic = Team('Slavic')
    #
    # arty_1 = BaseTank('80 CM SCHWERER GUSTAV KANONEN', TankType.ARTY)
    # player_1 = Player(arty_1, 'Player1')
    #
    # arty_2 = copy(arty_1)
    # player_2 = Player(arty_2, 'Player2')
    #
    # medium_1 = BaseTank('X24', TankType.MEDIUM)
    # player_3 = Player(medium_1, 'Player3')
    #
    # medium_2 = copy(medium_1)
    # player_4 = Player(medium_2, 'Player4')
    #
    # heavy_1 = BaseTank('CHAD TIGER', TankType.HEAVY)
    # player_5 = Player(heavy_1, 'Player5')
    #
    # heavy_2 = copy(heavy_1)
    # player_6 = Player(heavy_2, 'Player6')
    #
    # light_1 = BaseTank('A3', TankType.LIGHT)
    # player_7 = Player(light_1, 'Player7')
    #
    # light_2 = copy(light_1)
    # player_8 = Player(light_2, 'Player8')
    #
    # team_beacon.add_player(player_1)
    #
    # team_beacon.add_player(player_3)
    # team_beacon.add_player(player_5)
    # team_beacon.add_player(player_7)
    #
    # team_slavic.add_player(player_2)
    # team_slavic.add_player(player_4)
    # team_slavic.add_player(player_6)
    # team_slavic.add_player(player_8)
    #
    #
    # player_1.select_target(team_slavic)
    # player_3.select_target(team_slavic)
    # player_5.select_target(team_slavic)
    # player_7.select_target(team_slavic)
    #
    #
