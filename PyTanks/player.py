import random


class Player:

    def __init__(self, active_tank, nickname):
        if type(active_tank).__name__ != 'BaseTank':
            raise ValueError('Invalid tank')
        self.active_tank = active_tank
        self.nickname = nickname

    def select_target(self, other_team):

        if type(other_team).__name__ != 'Team':
            raise ValueError('Other team is invalid')

        # select only players with active tanks
        active_enemies = list(filter(lambda player: player.active_tank.alive, other_team.list_player))

        # arty are focused at the end
        arty_players = list(filter(lambda player: player.active_tank.tank_type == 5, active_enemies))
        non_arty_players = list(filter(lambda player: player.active_tank.tank_type != 5, active_enemies))

        if len(non_arty_players) != 0:
            target_player = non_arty_players[random.randint(0, len(non_arty_players) - 1)]
        else:
            target_player = arty_players[random.randint(0, len(arty_players) - 1)]

        print('%s targeting %s' % (self.nickname, target_player.nickname))
        return target_player


