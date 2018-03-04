import pygame
from pygame.locals import *
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
    windowwidth -= 300
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


class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        # Get the current mouse position. This returns the position
        # as a list of two numbers.
        pos = pygame.mouse.get_pos()

        # Fetch the x and y out of the list,
        # just like we'd fetch letters out of a string.
        # Set the player object to the mouse location
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    # Keeping Cursor stuff even if i don't use
    # cursor = drawing.Block(constants.WHITE, 10, 10)
    # all_sprites_list = pygame.sprite.Group()
    # all_sprites_list.add(cursor)
    # Put this back in game loop if use
    # all_sprites_list.update()
    # all_sprites_list.draw(display)


def get_indices(screenwidth, screenheight, tile_amount):
    # Get the mouse position then do calculation to get index of clicked tile
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x = int(mouse_x / (screenwidth / tile_amount))
    mouse_y = int(mouse_y / (screenheight / tile_amount))
    # If the mouse click is passed the furthest tile
    if mouse_x > tile_amount:
        mouse_x = tile_amount - 1
    if mouse_y > tile_amount:
        mouse_y = tile_amount - 1
    return mouse_x, mouse_y


def tile_info(tile):
    myfont = pygame.font.SysFont("monospace", 25)
    label_list = []
    # render text
    label1 = myfont.render("Owner: " + tile.owner, 1, (0, 0, 0))
    label2 = myfont.render("Terrain: " + tile.terrain, 1, (0, 0, 0))
    label3 = myfont.render("Population: " + str(tile.population), 1, (0, 0, 0))
    label4 = myfont.render("Contains: " + tile.contains, 1, (0, 0, 0))
    label_list.append(label1)
    label_list.append(label2)
    label_list.append(label3)
    label_list.append(label4)
    return label_list


def draw_text(display, label_list):
    text_y = 10
    for x in label_list:
        display.blit(x, (710, text_y))
        text_y += 30
