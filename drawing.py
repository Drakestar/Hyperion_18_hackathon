import tkinter
from tkinter import Tk, Canvas


# Given a terrain name it will return a color to be used
def terrain_color(terrain_name):
    return {
        'mountain': "grey",
        'grassland': "green",
        "forest": "forestgreen",
        "hills": '#FF9912',
        "freshwaterdeep": "darkslategray2",
        "freshwatershallow": "darkslategray1",
        "saltwatershallow": "deepskyblue2",
        "saltwaterdeep": "deepskyblue3",
        "desert": "goldenrod1",
        "swamp": "#3D9140",
    }[terrain_name]


# Draws the map given the tileset, window details, and window itself
def draw_map(tiles, windowwidth, windowheight, window):
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
            window.create_rectangle(x1, y1, x2, y2, fill=terrain_color(column.terrain), outline="")
            # Set the left corner to right corner x
            x1 = x2
        # Advance y to go down
        y1 = y2
        # Reset x location of boxes
        x1 = x2 = 0


# Create and return a window given height and width
def init(windowwidth, windowheight):
    # Initialize the window
    master = Tk()
    # Give it a title
    master.title("RPG Storyteller")
    # Initialize the canvas to put stuff on it
    w = Canvas(master, width=windowwidth, height=windowheight)
    w.pack()
    return w
