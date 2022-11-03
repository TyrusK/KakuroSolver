import cProfile
import time
from reader import reader
from tkinter import *


def main():
    board = reader("test_file.txt")
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
    board.square_size = square_size

    x_offset = int((screen_width - width) / 2)
    y_offset = int((screen_height - height) / 2)
    # print(f"width: {width}, height: {height}, x_offset: {x_offset}, y_offset: {y_offset}")
    root.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)

    canvas = Canvas(frame)
    board.canvas = canvas
    board.root = root

    board.draw()
    root.update()
    board.fill_cell_options2()
    board.finish_board()
    board.draw()
    # print(board)

    # Animation stuff
    """root.update()
    time.sleep(1)"""

    print("done")
    root.mainloop()


if __name__ == '__main__':
    # main()
    cProfile.run("main()")