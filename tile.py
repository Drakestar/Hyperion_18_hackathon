class Tile:
    coordinate = (-1, -1)
    terrain = "saltwaterdeep"
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
            submap.append(Tile((x, y), "saltwaterdeep", 0, "wild"))
        tilemap.append(submap)

    return tilemap

def generate_prebuilt_a():
    # tilemap is a list of lists representing a 2d grid of tiles
    tilemap = []

    for y in range(10):
        submap = []
        submap.append(Tile((x, y), "saltwaterdeep", 0, "wild"))
        submap.append(Tile((x, y), "desert", 0, "wild"))
        submap.append(Tile((x, y), "swamp", 0, "wild"))
        submap.append(Tile((x, y), "mountain", 0, "wild"))
        submap.append(Tile((x, y), "hills", 0, "wild"))
        submap.append(Tile((x, y), "forest", 0, "wild"))
        submap.append(Tile((x, y), "desert", 0, "wild"))
        submap.append(Tile((x, y), "saltwaterdeep", 0, "wild"))
        submap.append(Tile((x, y), "saltwaterdeep", 0, "wild"))
        submap.append(Tile((x, y), "saltwaterdeep", 0, "wild"))
        tilemap.append(submap)

    return tilemap
