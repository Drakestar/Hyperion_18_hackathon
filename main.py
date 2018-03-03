# Import statements
import pygame
from pygame.locals import *
import constants
import tile
import drawing


def main():
    # Start pygame and create the display at a start of 700x700
    pygame.init()
    display = pygame.display.set_mode((700, 700), 0, 32)
    display.fill(constants.WHITE)
    # Create map
    tile_set = tile.generate_tilemap(10)
    #
    #
    drawing.draw_map(tile_set, display)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
