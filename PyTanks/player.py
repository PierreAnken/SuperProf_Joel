import random


class Player:
    nicknames = ['Blacklight',
                 'OwlChick',
                 'CitarNosis',
                 'ThunderHawk',
                 'PowerGrab',
                 'Seismology',
                 'RichterScales',
                 'Palpebral',
                 'Maggotta',
                 'Myopia',
                 'MsMittens',
                 'Monstrum',
                 'PanzerElite',
                 'BatBoy',
                 'Slyrack']

    def __init__(self, active_tank, nickname=None):

        if not nickname:
            nickname = self.nicknames[random.randint(0, len(self.nicknames)-1)]
            nickname = f'{nickname}_{random.randint(1, 100)}'

        self.active_tank = active_tank
        self.nickname = nickname

    def select_target(self, other_team):

        if type(other_team).__name__ != 'Team':
            raise ValueError('Other team is invalid')

        # select only players with active tanks
        active_enemies = list(filter(lambda player: not player.active_tank.death, other_team.list_player))

        # arty are focused at the end
        arty_players = list(filter(lambda player: type(player.active_tank).__name__ == 'ArtyTank', active_enemies))
        non_arty_players = list(filter(lambda player: type(player.active_tank).__name__ != 'ArtyTank', active_enemies))

        if len(non_arty_players) != 0:
            target_player = non_arty_players[random.randint(0, len(non_arty_players) - 1)]
        else:
            target_player = arty_players[random.randint(0, len(arty_players) - 1)]

        print('%s targeting %s' % (self.nickname, target_player.nickname))
        return target_player
