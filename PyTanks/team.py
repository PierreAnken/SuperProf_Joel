
class Team:

    def __init__(self, name):
        self.name = name
        self.list_player = []

    def add_player(self, player):

        if player in self.list_player:
            raise ValueError('Player already team')

        if type(player).__name__ != 'Player':
            raise ValueError('Invalid player')

        print('Adding %s to team %s' % (player.nickname, self.name))
        self.list_player.append(player)

