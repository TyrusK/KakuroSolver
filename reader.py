import os
from cellType import CellType
from board import Board
from group import Group
from group import Cell
from direction import Direction


def reader(filename: str):
    cells = []
    groups = []
    if not (os.path.exists(filename) and os.access(filename, os.R_OK)):
        print(f"File \"{filename}\" could not be found")
        exit()
    with open(filename, "r") as file:
        line = file.readline()
        i = 0
        j = 0
        while line != "":
            line = line.replace(" ", "")
            split_line = line.split("|")
            if split_line[0] == "":
                split_line.pop(0)
            else:
                print("Invalid format, each line must begin with \"|\" character")
                exit()
            if split_line[-1] == "\n":
                split_line.pop(-1)
            else:
                print("Invalid format, each line must end with \"|\" character")
                exit()
            cell_row = []
            for i in range(len(split_line)):
                value = None
                try:
                    value = int(split_line[i])
                except ValueError:
                    pass
                if value is not None:
                    cell = Cell(i, j, value, None, None, CellType.SPACE)
                    cell_row.append(cell)
                elif split_line[i] == ".":
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
    j -= 1
    for g in groups:
        x = g.anchor.x
        y = g.anchor.y
        has_size = False
        while True:
            if g.direction == Direction.VERTICAL:
                y += 1
                if y > j or cells[y][x].cell_type == CellType.WALL:
                    break
                has_size = True
                g.add_cell(cells[y][x])
                cells[y][x].col = g
            elif g.direction == Direction.HORIZONTAL:
                x += 1
                if x > i or cells[y][x].cell_type == CellType.WALL:
                    break
                has_size = True
                g.add_cell(cells[y][x])
                cells[y][x].row = g
        if not has_size:
            if g.direction == Direction.VERTICAL:
                print("A column has zero size, invalid board")
            elif g.direction == Direction.HORIZONTAL:
                print("A row has zero size, invalid board")
            exit()
    board = Board(groups, cells, j + 1, i + 1)
    return board
