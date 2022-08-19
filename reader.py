from cellType import CellType
from board import Board
from group import Group
from group import Cell
from direction import Direction


def reader(filename: str):
    cells = []
    groups = []
    with open(filename, "r") as file:
        line = file.readline()
        j = 0
        while line != "":
            line = line.replace(" ", "")
            split_line = line.split("|")
            split_line.remove("")
            split_line.remove("\n")
            cell_row = []
            for i in range(len(split_line)):
                if split_line[i] == ".":
                    cell = Cell(i, j, None, None, None, CellType.SPACE)
                    cell_row.append(cell)
                else:
                    cell = Cell(i, j, None, None, None, CellType.WALL)
                    cell_row.append(cell)
                    group_pair = split_line[i].split("\\")
                    # print(f"\ni: {i},  j: {j}")
                    # print(f"cell: |{split_line[i]}|")
                    if group_pair[0] != "-":
                        # print(f"col: [{group_pair[0]}]")
                        group = Group([], Direction.VERTICAL, cell, int(group_pair[0]))
                        groups.append(group)
                    if group_pair[1] != "-":
                        # print(f"row: [{group_pair[1]}]")
                        group = Group([], Direction.HORIZONTAL, cell, int(group_pair[1]))
                        groups.append(group)
            cells.append(cell_row)
            line = file.readline()
            j += 1
    for g in groups:
        x = g.anchor.x
        y = g.anchor.y
        while True:
            if g.direction == Direction.VERTICAL:
                y += 1
                if y > j or cells[y][x].cell_type == CellType.WALL:
                    break
                g.add_cell(cells[y][x])
                cells[y][x].col = g
            elif g.direction == Direction.HORIZONTAL:
                x += 1
                if x > i or cells[y][x].cell_type == CellType.WALL:
                    break
                g.add_cell(cells[y][x])
                cells[y][x].col = g
    board = Board(groups, cells, j + 1, i + 1)
    return board
