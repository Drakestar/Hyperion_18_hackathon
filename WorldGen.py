import tile
import random
import numpy as np


def generate_terrain(world_map):
    terrain_list = ['mountain', 'hill', 'forest', 'grassland']
    exotic_probability = .05
    size = len(world_map) - 1
    for row in world_map:
        for tile in row:
            if tile.coordinate[0] == 0 or tile.coordinate[1] == 0 or tile.coordinate[0] == size or tile.coordinate[
                1] == size:
                tile.terrain = 'deep ocean'
            else:
                neighbors_list = get_neighbors(world_map, tile)
                if neighbors_list[0].terrain == neighbors_list[1].terrain:
                    neighbor_probability = .66
                    new_terrain = 1 - neighbor_probability
                    prob_list = [new_terrain, neighbor_probability]
                    choices = [1, 2]
                    selection = np.random.choice(choices, p=prob_list)

                else:
                    neighbor_probability_1 = .33
                    neighbor_probability_2 = .33
                    new_terrain = 1 - neighbor_probability_1 - neighbor_probability_2
                    prob_list = [new_terrain, neighbor_probability_1, neighbor_probability_2]
                    choices = [1, 2, 3]
                    selection = np.random.choice(choices, p=prob_list)

                if selection == 1:
                    tile.terrain = terrain_list[np.random_intergers() % 4]
                if selection == 2:
                    tile.terrain = neighbors_list[0].terrain
                if selection == 3:
                    tile.terrain = neighbors_list[1].terrain


def get_neighbors(world_map, tile):
    neighbors = [world_map[tile.coordinate[0] - 2][tile.coordinate[1] - 1], world_map[tile.coordinate[0] - 1][tile.coordinate[1] - 2]]
    return neighbors
