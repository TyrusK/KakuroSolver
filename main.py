from direction import Direction
from board_str import board_str
from reader import reader


if __name__ == '__main__':
    board = reader("test_file.txt")
    string = board_str(board)




    """
    for group in board.groups:
        print(f"({group.anchor.x}, {group.anchor.y})", end=", ")
        if group.direction == Direction.VERTICAL:
            print("Col", end=", ")
        elif group.direction == Direction.HORIZONTAL:
            print("Row", end=", ")
        print(f"Total: {group.total}", end=", ")
        print(f"len: {group.len}")
    """