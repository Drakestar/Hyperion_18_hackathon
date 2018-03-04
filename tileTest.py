import time

import npc
import tile
import nameGen

tiles = tile.Tile((0, 0), "plains", 0, "wild", "empty")
print(tiles.owner)

world_map = tile.generate_tilemap(20)

npcs = []

start = time.time()
i = 0
for i in range(10000):
    instance = npc.Npc()
    npcs.append(instance)
print(time.time() - start)