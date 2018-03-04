class Tile:
    coordinate = (-1, -1)
    terrain = "saltwaterdeep"
    population = 0
    owner = "wild"
    contains = []

    def __init__(self, coordinate: (int, int), terrain: str, population: int, owner: str, contains: str):
        self.coordinate = coordinate
        self.terrain = terrain
        self.population = population
        self.owner = owner
        self.contains = [] # this used to use contains


def generate_tilemap(map_scale: int):
    # tilemap is a list of lists representing a 2d grid of tiles
    tilemap = []

    for y in range(map_scale):
        submap = []
        for x in range(map_scale):
            submap.append(Tile((x, y), "saltwaterdeep", 0, "wild", "empty"))
        tilemap.append(submap)

    return tilemap
