from numpy import random
import Civilization
import nameGen


# Given the number of civilization and the world map places the 'capital' cities around the map
def generate_civs(civ_number, world_map):
    civ_list = []
    # Pull from civilization list and append the name to the civilization
    for i in range(civ_number):
        civ_list.append(Civilization.Civilization(nameGen.get_civilization_name(), 20, [], world_map))
    # For every civilization created find a suitable location for them and place them
    for civ in civ_list:
        location = find_suitable_location(world_map)
        # elf, name: str, type: str, population: int, is_capital: bool, influence: int, location: (int, int)
        holding = Civilization.Holding(nameGen.get_city_name(), 'village', civ, 20, True, 0, location)
        civ.holdings_list.append(holding)
        world_map[location[0]][location[1]].owner = civ.name
        world_map[location[0]][location[1]].contains.append(holding)
        update_city_influence(civ.name, location, world_map, 0)

    return civ_list


# Try to change the cities influence based on size
def update_city_influence(kingdom_name, location, world_map, influence):
    for x in range(-influence, influence + 1):
        for y in range(-influence, influence + 1):
            try:
                if location[0] + x >= 0 and location[1] + y >= 0:
                    world_map[location[0] + x][location[1] + y].owner = kingdom_name
            except IndexError:
                pass


def find_suitable_location(world_map):
    world_size = len(world_map)

    for i in range(0, 50):
        trial_location = (random.randint(1, (world_size - 2)), random.randint(1, (world_size - 2)))
        location = validate_city_location(world_map, trial_location)
        if location is not None:
            return location


def validate_city_location(world_map, trial_location):
    # print(trial_location[0], trial_location[1])
    if (world_map[trial_location[0]][trial_location[1]].terrain == "forest" or \
            world_map[trial_location[0]][trial_location[1]].terrain == "grassland" or \
            world_map[trial_location[0]][trial_location[1]].terrain == "hills") and \
            world_map[trial_location[0]][trial_location[1]].owner == "wild":
        return trial_location
    else:
        return None


def start_making_history(turns, civs, world_map):
    civilizations = generate_civs(civs, world_map)

    for i in range(turns):
        print("\n----- Generation " + str(i) + " -----")
        for civ in civilizations:
            civ.take_actions()
            civ.commit_expansions()

    print("\n----- Results -----")
    for civ in civilizations:
        print('Name:', civ.name)
        print('Population:', civ.total_population)
        print('Number of holding:', len(civ.holdings_list))
