import numpy as np
import nameGen


class Civilization:
    name = 'null'
    total_population = 0
    holdings_list = []

    def __init__(self, name: str, total_population: str, holdings_list: list):
        self.name = name
        self.total_population = total_population
        self.holdings_list = holdings_list

    def take_actions(self, map):
        expand_list = []
        for holding in self.holdings_list:
            location = holding.find_valid_neighbor(map)
            city = holding.take_action(location)
            if city is not None:
                map[location[0]][location[1]].contains.append(city.type)
                expand_list.append(city)
            self.total_population += holding.population

        print(self.name, 'has a population of ', self.total_population)
        self.holdings_list.extend(expand_list)


class Holding:
    name = 'null'
    type = 'village'
    population = 0
    is_capital = False
    influence = 0
    location = (0, 0)

    def __init__(self, name: str, type: str, population: int, is_capital: bool, influence: int, location: tuple):
        self.name = name
        self.population = population
        self.type = type
        self.is_capital = is_capital
        self.influence = influence
        self.location = location

    def stay_put(self):
        exponent = np.random.random()  # random float between 0 and 1
        self.population = int(round((self.population * np.e ** exponent)))  # population growth function
        if self.population < 200:
            self.type = 'village'
        elif self.population < 2000:
            self.type = 'town'
            if not self.is_capital:
                self.influence = 1
        elif self.population < 20000:
            self.type = 'city'
            if not self.is_capital:
                self.influence = 2
        else:
            self.type = 'metropolis'
            if not self.is_capital:
                self.influence = 3
        print(self.name, 'is now a', self.type, 'with a population of', self.population)

    def expand(self, location):
        self.population -= 20
        print(self.name, 'expanded, population =', self.population)
        # self, name: str, type: str, population: int, is_capital: bool, influence: int, location: (int, int)
        if location is not None:
            return Holding(nameGen.get_city_name(), 'village', 20, False, 0, location)
        else:
            self.stay_put()

    def take_action(self, location):
        if self.population < 100:
            self.stay_put()
        else:
            choices = [1, 2]
            if self.type == 'town':
                selection = np.random.choice(choices, p=[.8, .2])  # 80% Chance of stay put, 20% chance of expanding
            elif self.type == 'city':
                selection = np.random.choice(choices, p=[.5, .5])  # 50/50 chance of action
            else:
                selection = np.random.choice(choices, p=[.25, .75])  # 75% chance of expansion
            if selection == 1:
                self.stay_put()
            else:
                return self.expand(location)

    def find_valid_neighbor(self, world_map):
        neighbors_list = []
        influence = self.influence
        for x in range(-influence, influence + 1):
            for y in range(-influence, influence + 1):
                if x == -influence or x == influcence + 1 or y == influence or y == influence + 1:
                    try:
                       neighbors_list.append(world_map[self.location[0] + x][slef.location[1] + y])
                    except IndexError:
                        pass
        for n in neighbors_list:
            if n.owner != 'wild' or 'water' in n.terrain:
                neighbors_list.remove(n)
        if len(neighbors_list) > 0:
            return neighbors_list[
                np.random.random_integers(0, len(neighbors_list) - 1)]  # gets random selection from the
        else:
            return None
    # location list
