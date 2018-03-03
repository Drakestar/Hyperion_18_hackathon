# Import statements
import tkinter
from tkinter import Tk, Canvas
import drawing

test_tiles = [["mountain", "grassland", "forest", "hills"],
            ["freshwaterdeep", "freshwatershallow", "saltwatershallow", "saltwaterdeep"],
            ["desert", "swamp", "forest", "hills"]]


def main():
    width = 700
    height = 700
    # Initialize the window
    master = Tk()
    # Give it a title
    master.title("RPG Storyteller")
    # Initialize the canvas to put stuff on it
    w = Canvas(master, width=width, height=height)
    w.pack()
    drawing.draw_map(test_tiles, width, height, w)
    w.mainloop()
    # Start drawing and doing everything


if __name__ == "__main__":
    main()
