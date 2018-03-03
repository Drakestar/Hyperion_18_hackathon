# Import statements
import tkinter
from tkinter import Tk, Canvas


def main():
    # Initialize the window
    master = Tk()
    # Give it a title
    master.title("RPG Storyteller")
    # Initialize the canvas to put stuff on it
    w = Canvas(master, width=250, height=200)

    # Start drawing and doing everything
    master.mainloop()


if __name__ == "__main__":
    main()
