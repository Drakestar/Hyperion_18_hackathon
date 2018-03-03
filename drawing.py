import pygame
import constants


# Given a terrain name it will return a color to be used
def terrain_color(terrain_name):
    return {
        'mountain': constants.MOUNTAIN,
        'grassland': constants.GRASSLAND,
        "forest": constants.FOREST,
        "hills": constants.HILLS,
        "freshwaterdeep": constants.FRESHDEEP,
        "freshwatershallow": constants.FRESHSHALLOW,
        "saltwatershallow": constants.SALTSHALLOW,
        "saltwaterdeep": constants.SALTDEEP,
        "desert": constants.DESERT,
        "swamp": constants.SWAMP,
    }[terrain_name]


# Draws the map given the tileset, window details, and window itself
def draw_map(tiles, display):
    windowwidth, windowheight = pygame.display.get_surface().get_size()
    # Set Square corners to 0
    x1 = y1 = x2 = y2 = 0
    # Go through each row of the tileset
    for row in tiles:
        # The opposite corners y value updates
        y2 += windowheight / len(tiles)
        # Go through every column in the row
        for column in row:
            # Advance the location of the bottom right corner of square
            x2 += windowwidth / len(row)
            # Create the rectangle with no outline on squares
            pygame.draw.rect(display, terrain_color(column.terrain), (x1, y1, x2, y2))
            # Set the left corner to right corner x
            x1 = x2
        # Advance y to go down
        y1 = y2
        # Reset x location of boxes
        x1 = x2 = 0
