import tile
import drawing
import WorldGen
import nameGen

tiles = tile.Tile((0, 0), "plains", 0, "wild")
print(tiles.owner)

world_map = tile.generate_tilemap(20)

while True:
    print(nameGen.get_first_name_human_male())

while True:
    for row in world_map:
        temp_str = ""
        for tile in row:
            temp_str = temp_str + "\t(" + str(tile.coordinate[0]) + "," + str(tile.coordinate[1]) + ")"
        print(temp_str + "\n")

    WorldGen.generate_terrain(world_map)

    w = drawing.init(720, 720)
    drawing.draw_map(world_map, w)
    w.mainloop()
