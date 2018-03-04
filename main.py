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
    tile_map = tile.generate_tilemap(10)
    WorldGen.generate_terrain(tile_map)
    # Constants
    width, height = pygame.display.get_surface().get_size()
    # Main "game" loop
    while True:
        # Draw map
        drawing.draw_map(tile_map, display)
        # Look through all events
        for event in pygame.event.get():
            # Quit
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                # print event.button
                mouse_x, mouse_y = pygame.mouse.get_pos()
                mouse_x = int(mouse_x / (width / len(tile_map)))
                mouse_y = int(mouse_y / (height / len(tile_map)))
                print(tile_map[mouse_y][mouse_x].terrain)
        pygame.display.update()


if __name__ == "__main__":
    main()
