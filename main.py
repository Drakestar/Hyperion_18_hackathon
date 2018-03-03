# Import statements
import tkinter
from tkinter import Tk, Canvas
import drawing


def main():
    # Create and initialize window from drawing file
    w = drawing.init(700, 700)
    
    # Calls to draw file

    # Main loop
    w.mainloop()


if __name__ == "__main__":
    main()
