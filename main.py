from direction import Direction
from reader import reader


if __name__ == '__main__':
    board = reader("wrong_board.txt")
    print(f"[\n{board}\n]")

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