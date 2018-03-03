import tkinter
from tkinter import Tk, Canvas

width = 700
height = 700


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


def draw_map(tiles, width, height, window):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    for row in tiles:
        y2 += height / len(tiles)
        for column in row:
            x2 += width / len(row)
            window.create_rectangle(x1, y1, x2, y2, fill=terrain_color(column), outline="")
            x1 = x2
        y1 = y2
        x1 = 0
        x2 = 0


def init():
    # Initialize the window
    master = Tk()
    # Give it a title
    master.title("RPG Storyteller")
    # Initialize the canvas to put stuff on it
    w = Canvas(master, width=width, height=height)
    w.pack()
    return w
