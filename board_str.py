from board import Board
from cellType import CellType
from direction import Direction
from group import Group


def board_str(board: Board):
    string = ""
    x = 0
    y = 0
    group_num = 0
    max_group = len(board.groups)
    group = board.groups[group_num]
    for line in board.cells:
        for cell in line:
            if group_num < max_group:
                group = board.groups[group_num]
            if cell.cell_type == CellType.WALL:
                string += "|"
                if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.VERTICAL:
                    string += f"{num_string(group)}"
                    group_num += 1
                    if group_num < max_group:
                        group = board.groups[group_num]
                else:
                    string += " -"
                string += "\\"
                if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.HORIZONTAL:
                    string += f"{num_string(group)}"
                    group_num += 1
                else:
                    string += "- "
            else:
                string += "|  .  "
            x += 1
            if x > board.width - 1:
                string += "|\n"
                x = 0
        y += 1
    return string


def num_string(group: Group):
    num = group.total
    direction = group.direction
    if num > 9:
        return str(num)
    if direction == Direction.VERTICAL:
        return f" {str(num)}"
    return f"{str(num)} "
