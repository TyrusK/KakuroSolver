from direction import Direction
from reader import reader
from tkinter import *

if __name__ == '__main__':
    board = reader("test_file.txt")
    board.fill_cell_options()
    board.find_values()
    print(board)
    square_size = 80

    root = Tk()
    root.resizable(width=False, height=False)
    root.title("Kakuro")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight() - 60
    width = square_size * board.width + 9
    if width > screen_width:
        square_size = int(screen_width / board.width)
    height = square_size * board.height + 9
    if height > screen_height:
        square_size = int(screen_height / board.height)
        height = square_size * board.height + 9
    width = square_size * board.width + 9

    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)
    print(f"width: {width}, height: {height}, x_offset: {x_offset}, y_offset: {y_offset}")
    root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

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