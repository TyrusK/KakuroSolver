from cell import Cell
from cellType import CellType
from board import Board
from group import Group
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
            for i in range(len(split_line)):
                if split_line[i] == ".":

                    cell = Cell(i, j, None, row, col, CellType.SPACE)
                    cells.append(cell)
                else:
                    cell = Cell(i, j, None, None, None, CellType.WALL)
                    group_pair = split_line[i].split("\\")
                    if group_pair[0] != "-":
                        group = Group(, Direction.VERTICAL, cell, )
                        groups.append(group)
                    if group_pair[1] != "-":
                        group = Group(, Direction.HORIZONTAL, cell, )
                        groups.append(group)
            line = file.readline()
            j += 1
    board = Board(groups, cells, j + 1, i + 1)
    return board