import random
import numpy as np
import nameGen
import HistoryGen


class Civilization:
    name = 'null'
    total_population = 0
    holdings_list = []
    expand_list = []
    world_map = [[]]

    def __init__(self, name: str, total_population: int, holdings_list: list, world_map):
        self.name = name
        self.total_population = total_population
        self.holdings_list = holdings_list
        self.world_map = world_map

    def take_actions(self):
        print(self.name)
        for holding in self.holdings_list:
            holding.take_action()

    def commit_expansions(self):
        self.holdings_list.extend(self.expand_list)


class Holding:
    name = 'null'
    settlement_type = 'village'
    held_by = None
    population = 0
    is_capital = False
    influence = 0
    location = (0, 0)

    def __init__(self, name, settlement_type, held_by, population, is_capital, influence, location):
        self.name = name
        self.settlement_type = settlement_type
        self.held_by = held_by
        self.population = population
        self.is_capital = is_capital
        self.influence = influence
        self.location = location

    def take_action(self):
        self.held_by.commit_expansions()
        self.held_by.expand_list = []
        if self.population < 100:
            self.stay_put()
        else:
            choices = [1, 2]
            if self.settlement_type == 'town':
                selection = np.random.choice(choices, p=[.8, .2])  # 80% Chance of stay put, 20% chance of expanding
            elif self.settlement_type == 'city':
                selection = np.random.choice(choices, p=[.5, .5])  # 50/50 chance of action
            else:
                selection = np.random.choice(choices, p=[.25, .75])  # 75% chance of expansion
            if selection == 1:
                self.stay_put()
            else:
                self.expand()

    def stay_put(self):
        exponent = np.random.random()  # random float between 0 and 1
        print(int(round((self.population * np.e ** exponent))))
        self.population = int(round((self.population * np.e ** exponent)))  # population growth function
        if self.population < 200:
            self.settlement_type = 'village'
            self.held_by.world_map[self.location[0]][self.location[1]].contains = []
            self.held_by.world_map[self.location[0]][self.location[1]].contains.append(self)
        elif self.population < 2000:
            self.settlement_type = 'town'
            self.influence = 1
            self.held_by.world_map[self.location[0]][self.location[1]].contains = []
            self.held_by.world_map[self.location[0]][self.location[1]].contains.append(self)
            HistoryGen.update_city_influence(self.held_by.name, self.location, self.held_by.world_map, self.influence)
        elif self.population < 20000:
            self.settlement_type = 'city'
            self.influence = 2
            self.held_by.world_map[self.location[0]][self.location[1]].contains = []
            self.held_by.world_map[self.location[0]][self.location[1]].contains.append(self)
            HistoryGen.update_city_influence(self.held_by.name, self.location, self.held_by.world_map, self.influence)
        else:
            self.settlement_type = 'metropolis'
            self.influence = 3
            self.held_by.world_map[self.location[0]][self.location[1]].contains = []
            self.held_by.world_map[self.location[0]][self.location[1]].contains.append(self)
            HistoryGen.update_city_influence(self.held_by.name, self.location, self.held_by.world_map, self.influence)

        print(" - " + self.name + " is growing, population = " + str(self.population))

    def expand(self):
        self.population -= 20
        location = self.find_suitable_nearby_location(self.influence + 4)
        if location is not None:
            holding = Holding(nameGen.get_city_name(), 'village', self.held_by, 20, True, 0, location)
            self.held_by.expand_list.append(holding)
            self.held_by.world_map[location[0]][location[1]].owner = self.held_by.name
            self.held_by.world_map[location[0]][location[1]].contains.append(holding)
            HistoryGen.update_city_influence(self.held_by.name, location, self.held_by.world_map, 0)
        else:
            # print("No Suitable Expansions Found")
            pass
        print(" - " + self.name + " is settling new territory, population = " + str(self.population))

    def find_suitable_nearby_location(self, expansion_range):
        for i in range(0, 50):
            x = random.randint(-expansion_range, expansion_range)
            y = random.randint(-expansion_range, expansion_range)
            trial_location = (x + self.location[0], y + self.location[1])
            if self.location[0] + x > 0 and self.location[1] + y > 0:
                try:
                    location = self.validate_city_location(trial_location)
                except:
                    location = None
                    # print("BAD BAD BAD")
                if location is not None:
                    return location
        return None

    def validate_city_location(self, trial_location):
        # print(trial_location[0], trial_location[1])
        if (self.held_by.world_map[trial_location[0]][trial_location[1]].terrain == "forest" or \
            self.held_by.world_map[trial_location[0]][trial_location[1]].terrain == "grassland" or \
            self.held_by.world_map[trial_location[0]][trial_location[1]].terrain == "hills") and \
                self.held_by.world_map[trial_location[0]][trial_location[1]].owner == "wild":
            return trial_location
        else:
            return None

