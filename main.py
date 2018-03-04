# Import statements
import pygame
from pygame.locals import *
import tile
import WorldGen
import drawing


def main():
    # Start pygame and create the display at a start of 700x700
    pygame.init()
    pygame.display.set_caption("RPG Storyteller")
    display = pygame.display.set_mode((700, 700), 0, 32)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create map
    tile_map = tile.generate_tilemap(50)
    WorldGen.generate_terrain(tile_map)
    # Constants
    # Main "game" loop
    while True:
        # Draw map
        drawing.draw_map(tile_map, display)
        # Look through all events
        for event in pygame.event.get():
            # Quit
            if event.type == QUIT:
                pygame.quit()
        pygame.display.update()


if __name__ == "__main__":
    main()
