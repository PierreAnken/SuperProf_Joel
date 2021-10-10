from PyTanks.game import Game
from PyTanks.utils import get_random_element_from_list

if __name__ == '__main__':

    my_game = Game()

    for i in range(1, 10):
        player_shooting = get_random_element_from_list(my_game.team_1.list_player)
        target_player = player_shooting.select_target(my_game.team_2)
        player_shooting.active_tank.inflict_damage(target_player.active_tank)

        player_shooting = get_random_element_from_list(my_game.team_2.list_player)
        target_player = player_shooting.select_target(my_game.team_1)
        player_shooting.active_tank.inflict_damage(target_player.active_tank)
