import random
from copy import copy

from PyTanks.Tanks.tank_factory import TankFactory
from PyTanks.wot_api import WotAPI


class Game:

    def __init__(self):
        factory = TankFactory()
        factory.load_tank_from_json(1)

        tank_1 = copy(factory.tank_list[random.randint(0, len(factory.tank_list)-1)])
        tank_2 = copy(factory.tank_list[random.randint(0, len(factory.tank_list)-1)])

        print(f'Combat started between {tank_1.model} and {tank_2.model}')
        while not tank_2.death and not tank_1.death:
            tank_1.inflict_damage(tank_2)
            tank_2.inflict_damage(tank_1)
