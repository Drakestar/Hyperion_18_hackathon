class Tile:
    terrain = "plains"
    population = 0
    owner = "wild"

    def __init__(self, terrain:str, population:int, owner:str):
        self.terrain = terrain
        self.population = population
        self.owner = owner
