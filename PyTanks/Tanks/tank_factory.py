from PyTanks.Tanks.arty_tank import ArtyTank
from PyTanks.Tanks.heavy_tank import HeavyTank
from PyTanks.Tanks.light_tank import LightTank
from PyTanks.Tanks.medium_tank import MediumTank
from PyTanks.Tanks.td_tank import TDTank
from PyTanks.wot_api import WotAPI


class TankFactory:
    tank_list = []

    def getTank(self, tank_data):

        tank_type = tank_data.get('type')

        if tank_type == 'lightTank':
            return LightTank(tank_data)
        elif tank_type == 'heavyTank':
            return HeavyTank(tank_data)
        elif tank_type == 'AT-SPG':
            return TDTank(tank_data)
        elif tank_type == 'mediumTank':
            return MediumTank(tank_data)
        else:
            return ArtyTank(tank_data)

    def load_tank_from_json(self, tier):

        api = WotAPI()
        list_tank_dict = api.get_tank_list(tier)
        factory = TankFactory()

        for tank_data in list_tank_dict.values():
            new_tank = factory.getTank(tank_data)
            self.tank_list.append(new_tank)
