import random


def get_random_element_from_list(my_list):
    return my_list[random.randint(0, len(my_list)-1)]