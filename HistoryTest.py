import HistoryGen
import Civilization
import WorldGen
import tile

world_map = tile.generate_tilemap(20)
WorldGen.generate_terrain(world_map)

HistoryGen.start_making_history(10, 4, world_map)
