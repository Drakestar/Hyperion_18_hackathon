import time

import HistoryGen
import npc
import tile
import nameGen

tiles = tile.Tile((0, 0), "plains", 0, "wild", "empty")
print(tiles.owner)

world_map = tile.generate_tilemap(20)

HistoryGen.start_making_history(1, 4, world_map)


#npcs = []

#start = time.time()
#i = 0
#for i in range(10000):
#    instance = npc.Npc()
#    print(str(instance))
#    npcs.append(instance)
#print(time.time() - start)