import tile

tiles = tile.Tile((0,0), "plains", 0, "wild")
print(tiles.owner)

world_map = tile.generate_tilemap(5)

for row in world_map:
    temp_str = ""
    for tile in row:
        temp_str = temp_str + "\t(" + str(tile.coordinate[0]) + "," + str(tile.coordinate[1]) + ")"
    print(temp_str + "\n")
