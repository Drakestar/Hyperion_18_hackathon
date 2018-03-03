class Tile:
    coordinate = (-1, -1)
    terrain = "deep ocean"
    population = 0
    owner = "wild"

    def __init__(self, coordinate: (int, int), terrain: str, population: int, owner: str):
        self.coordinate = coordinate
        self.terrain = terrain
        self.population = population
        self.owner = owner


def generate_tilemap(map_scale: int):
    # tilemap is a list of lists representing a 2d grid of tiles
    tilemap = []

    for y in range(map_scale):
        submap = []
        for x in range(map_scale):
            submap.append(Tile((x, y), "deep ocean", 0, "wild"))
        tilemap.append(submap)

    return tilemap
