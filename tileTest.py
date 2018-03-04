import tile
import drawing
import WorldGen
import nameGen

tiles = tile.Tile((0, 0), "plains", 0, "wild", "empty")
print(tiles.owner)

world_map = tile.generate_tilemap(20)

while True:
    print(nameGen.get_first_name_human_female())