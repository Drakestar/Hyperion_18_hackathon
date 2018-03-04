from numpy import random

import Civilization
import nameGen


def generate_civs(civ_number, world_map):
    civ_list = []
    for i in range(civ_number):
        civ_list.append(Civilization.Civilization(nameGen.get_civilization_name(), 20, []))

    for civ in civ_list:
        location = find_suitable_location(world_map)
        # elf, name: str, type: str, population: int, is_capital: bool, influence: int, location: (int, int)
        civ.holdings_list.append(Civilization.Holding(nameGen.get_city_name(), 'village', 20, True, 3, location))

    return civ_list


def find_suitable_location(world_map):
    valid_location = False
    world_size = len(world_map)

    while not valid_location:
        trial_location = (random.randint(1, (world_size - 1)), random.randint(1, (world_size - 1)))
        if world_map[trial_location[0]][trial_location[1]].terrain == "forest" or \
            world_map[trial_location[0]][trial_location[1]].terrain == "grassland" or \
            world_map[trial_location[0]][trial_location[1]].terrain == "hills":

            world_map[trial_location[0]][trial_location[1]].contains.append("village")
            valid_location = True

            return trial_location


def start_making_history(turns, civs, world_map):
    civilizations = generate_civs(civs, world_map)

    for i in range(turns):
        for civ in civilizations:
            civ.take_actions(world_map)

    for civ in civilizations:
        print('Name:', civ.name)
        print('Population:', civ.total_population)
        print('Number of holding:', len(civ.holdings_list))
