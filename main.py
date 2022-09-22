from direction import Direction
from reader import reader
from tkinter import *

if __name__ == '__main__':
    board = reader("test_file.txt")
    board.fill_cell_options()
    print(board)
    square_size = 80

    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Kakuro")
    width = square_size * board.width + 9
    height = square_size * board.height + 9
    root.geometry(f"{width}x{height}+500+200")

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(frame)
    board.draw(canvas, square_size, width, height)

    root.mainloop()

    """
    for group in board.groups:
        print(f"({group.anchor.x}, {group.anchor.y})", end=", ")
        if group.direction == Direction.VERTICAL:
            print("Col", end=", ")
        elif group.direction == Direction.HORIZONTAL:
            print("Row", end=", ")
        print(f"Total: {group.total}", end=", ")
        print(f"size: {group.size}")
    """