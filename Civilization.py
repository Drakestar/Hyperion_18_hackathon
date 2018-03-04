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
            city = holding.take_action()
            if city is not None:
                expand_list.append(city)
            self.total_population += holding.population

        print(self.name, 'has a population of ', self.total_population)
        self.holdings_list.extend(expand_list)


class Holding:
    name = 'null'
    type = 'village'
    population = 0
    is_capital = false
    influence = 0
    location = (0, 0)

    def __init__(self, name: str, type: str, population: int, is_capital: bool, influence: int, location: pair):
        self.name = name
        self.population = population
        self.type = type
        self.is_capital = is_capital
        self.influence = influence
        self.location = location

    def stay_put(self):
        exponent = np.random.random()
        self.population = int(round((self.population * np.e ** exponent)))
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
        print(self.name, 'is now a ', self.type, 'with a population of ', self.population)

    def expand(self):
        self.population -= 20
        print(self.name, 'expanded, population = ', self.population)
        return Holding(nameGen.get_city_name(), 'village', 20)

    def take_action(self):
        if self.population < 100:
            self.stay_put()
        else:
            choices = [1, 2]
            if self.type == 'town':
                selection = np.random.choice(choices, p=[.8, .2])
            elif self.type == 'city':
                selection = np.random.choice(choices, p=[.5, .5])
            else:
                selection = np.random.choice(choices, p=[.25, .75])
            if selection == 1:
                self.stay_put()
            else:
                return self.expand()

    def find_valid_neighbor(self, map):
        x_position = self.location[0] - 1
        y_position = self.location[1] - 1

        inf = self.influence #need influence to check the proper tiles

        try:
            north = map[x_position][y_position + inf].owner
        except IndexError:
            north = None
        try:
            south = map[x_position][y_position - inf].owner
        except IndexError:
            south = None
        try:
            east = map[x_position + inf][y_position].owner
        except IndexError:
            east = None
        try:
            west = map[x_position - inf][y_position].owner
        except IndexError:
            west = None

