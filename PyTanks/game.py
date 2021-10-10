
from PyTanks.Tanks.tank_factory import TankFactory
from PyTanks.team import Team


class Game:

    def __init__(self):
        factory = TankFactory()
        factory.load_tanks_from_api(1)
        self.team_1 = Team('team Conqueror')
        self.team_2 = Team('Panzer Elite')
        self.team_1.generate_players(15, factory.get_tank_list())
        self.team_2.generate_players(15, factory.get_tank_list())






