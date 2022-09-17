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
        have_width = False
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
                print("Invalid format, each line must end with \"|\" character and the last line must be blank")
                exit()
            cell_row = []
            for i in range(len(split_line)):
                value = None
                try:
                    value = int(split_line[i])
                except ValueError:
                    pass
                if value is not None:
                    if 0 < value < 10:
                        cell = Cell(i, j, None, CellType.SPACE)
                        cell_row.append(cell)
                    else:
                        print("Invalid format, values must be single digits above zero")
                        exit()
                elif split_line[i] == ".":
                    cell = Cell(i, j, None, CellType.SPACE)
                    cell_row.append(cell)
                else:
                    cell = Cell(i, j, None, CellType.WALL)
                    cell_row.append(cell)
                    group_pair = split_line[i].split("\\")
                    # print(f"\ni: {i},  j: {j}")
                    # print(f"cell: |{split_line[i]}|")
                    if group_pair[0] != "-":
                        # print(f"col: [{group_pair[0]}]")
                        try:
                            group = Group([], Direction.VERTICAL, cell, int(group_pair[0]))
                        except ValueError:
                            print("Invalid cell format")
                            exit()
                        groups.append(group)
                    if group_pair[1] != "-":
                        # print(f"row: [{group_pair[1]}]")
                        try:
                            group = Group([], Direction.HORIZONTAL, cell, int(group_pair[1]))
                        except ValueError:
                            print("Invalid cell format")
                            exit()
                        groups.append(group)
            if not have_width:
                width = i
                have_width = True
            if have_width and i != width:
                print("Invalid format, inconsistent width")
                exit()
            cells.append(cell_row)
            line = file.readline()
            j += 1
    j -= 1
    for g in groups:
        x = g.anchor.x
        y = g.anchor.y
        index = 0
        has_size = False
        while True:
            if g.direction == Direction.VERTICAL:
                y += 1
                if y > j or cells[y][x].cell_type == CellType.WALL:
                    break
                has_size = True
                g.add_cell(cells[y][x])
                cells[y][x].col = g
                cells[y][x].col_index = index
            elif g.direction == Direction.HORIZONTAL:
                x += 1
                if x > i or cells[y][x].cell_type == CellType.WALL:
                    break
                has_size = True
                g.add_cell(cells[y][x])
                cells[y][x].row = g
                cells[y][x].row_index = index
            index += 1
        if not has_size:
            if g.direction == Direction.VERTICAL:
                print("A column has zero size, invalid board")
            elif g.direction == Direction.HORIZONTAL:
                print("A row has zero size, invalid board")
            exit()
        min_total = g.size * (g.size + 1) * 0.5
        max_total = g.size * (19 - g.size) * 0.5
        group_type = "row"
        if g.direction == Direction.VERTICAL:
            group_type = "column"
        if g.total < min_total:
            print(f"The sum for a {group_type} of length {g.size} cannot be less than {int(min_total)}")
            exit()
        if g.total > max_total:
            print(f"The sum for a {group_type} of length {g.size} cannot be greater than {int(max_total)}")
            exit()
    for cell_line in cells:
        for current_cell in cell_line:
            if current_cell.cell_type == CellType.SPACE:
                if current_cell.row is None:
                    print("A row has no defined value, invalid board")
                    exit()
                if current_cell.col is None:
                    print("A column has no defined value, invalid board")
                    exit()
    board = Board(groups, cells, j + 1, i + 1)
    return board
