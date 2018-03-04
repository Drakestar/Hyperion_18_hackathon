# Import statements
import pygame
import sys
import constants
from pygame.locals import *
import tile
import WorldGen
import drawing


def main():
    # Start pygame and create the display at a start of 700x700
    pygame.init()
    pygame.display.set_caption("RPG Storyteller")
    display = pygame.display.set_mode((1000, 700), 0, 32)
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    # Create map
    tile_map = tile.generate_tilemap(constants.WORLDSIZE)
    WorldGen.generate_terrain(tile_map)
    # Constants
    width, height = pygame.display.get_surface().get_size()
    width -= 300
    label_list = []
    myfont = pygame.font.SysFont("monospace", 25)
    label1 = myfont.render("YES", 1, (0, 0, 0))
    label2 = myfont.render("NO", 1, (0, 0, 0))
    label_list.append(label1)
    label_list.append(label2)
    loop_var = True
    while loop_var:
        # Draw map
        drawing.draw_map(tile_map, display)
        pygame.draw.rect(display, constants.GRAY, constants.SQUAREOFTRUTH)
        display.blit(label1, (835, 175))
        display.blit(label2, (835, 525))
        # Look through all events
        for event in pygame.event.get():
            # Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # User clicks a square it gives information
            if event.type == MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x > 700:
                    if mouse_y > 350:
                        WorldGen.generate_terrain(tile_map)
                    else:
                        loop_var = False
        # Draw the text when tile clicked
        #drawing.draw_text(display, label_list)
        pygame.display.update()
    # Main "game" loop
    while True:
        # Draw map
        drawing.draw_map(tile_map, display)
        pygame.draw.rect(display, constants.GRAY, constants.SQUAREOFTRUTH)
        # Look through all events
        for event in pygame.event.get():
            # Quit
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # User clicks a square it gives information
            if event.type == MOUSEBUTTONDOWN:
                tile_x, tile_y = drawing.get_indices(width, height, len(tile_map))
                print(tile_x, tile_y, len(tile_map))
                label_list = drawing.tile_info(tile_map[tile_y][tile_x])
        # Draw the text when tile clicked
        drawing.draw_text(display, label_list)
        pygame.display.update()


if __name__ == "__main__":
    main()
