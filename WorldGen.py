import numpy as np


# Generate terrains given a list of list of tiles
def generate_terrain(world_map):
    # List of 'normal' terrain
    terrain_list = ['mountain', 'hills', 'forest', 'grassland', 'hills', 'forest', 'grassland']
    # List of 'exotic' terrains
    exotic_list = ['swamp', 'desert', 'freshwaterdeep', 'freshwatershallow']
    exotic_probability = .05
    # Size of world so no out of bounds
    size = len(world_map) - 1
    # For loops that go through every tile
    for i_y, row in enumerate(world_map):
        for i_x, tile in enumerate(row):
            # Check if edge and turn into Deep saltwater
            if tile.coordinate[0] == 0 or tile.coordinate[1] == 0 or tile.coordinate[0] == size or tile.coordinate[1] == size:
                tile.terrain = 'saltwaterdeep'
            # Otherwise the terrain is in the center
            else:
                # Get list of neighbors that have already been made
                neighbors_list = get_neighbors(world_map, tile, i_y, i_x)
                # If the above neighbor is the same as left neighbor the chance of same as neighbors is 66%
                if neighbors_list[0].terrain == neighbors_list[1].terrain:
                    neighbor_probability = .66
                    # If the above neighbor is Saltwater lower the probability of taking it
                    if neighbors_list[0].terrain == 'saltwaterdeep':
                        neighbor_probability = .2
                    # The probability of a new terrain is the opposite of the chance of being it's neighbor
                    new_terrain = 1 - neighbor_probability
                    # The two choice based on probilities above
                    prob_list = [new_terrain, neighbor_probability]
                    # Given the choices numpy will choose from choices with chosen probabilities
                    choices = [1, 2]
                    selection = np.random.choice(choices, p=prob_list)
                # If both neighbors are not equal
                else:
                    # Equal chance of taking from either neighbor
                    neighbor_probability_1 = .33
                    neighbor_probability_2 = .33
                    # If one of the neighbors is Deep Saltwater lower chance of inheriting from it
                    if neighbors_list[0].terrain == 'saltwaterdeep':
                        neighbor_probability_1 = .2
                    if neighbors_list[1].terrain == 'saltwaterdeep':
                        neighbor_probability_2 = .2
                    # The probability of getting a new terrain is equal to the opposite of neighbor 1 and 2
                    new_terrain = 1 - neighbor_probability_1 - neighbor_probability_2
                    prob_list = [new_terrain, neighbor_probability_1, neighbor_probability_2]
                    choices = [1, 2, 3]
                    selection = np.random.choice(choices, p=prob_list)

                # Select from random new terrain 'normal' terrains
                if selection == 1:
                    # Do another selection to do a random new exotic terrain
                    rarity = [1, 2]
                    selection2 = np.random.choice(rarity, p=[1-exotic_probability, exotic_probability])
                    if selection2 == 1:
                        tile.terrain = terrain_list[np.random.random_integers(0, 10000000) % 7]
                    else:
                        print(np.random.random_integers(0, 100000) % 4)
                        tile.terrain = exotic_list[np.random.random_integers(0, 1000000) % 4]
                # Select neighbor terrain
                elif selection == 2:
                    tile.terrain = neighbors_list[0].terrain
                # Select neighbor terrain
                else:
                    tile.terrain = neighbors_list[1].terrain


# Get already initialized neighbors 0 = above, 1 = left neighbor
def get_neighbors(world_map, tile, row, col):
    neighbors = [world_map[row - 1][col],
                 world_map[row][col - 1]]
    return neighbors
