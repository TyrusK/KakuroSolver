from direction import Direction
from cellType import CellType
from typing import Optional


class Cell:
    def __init__(self, x: int, y: int, value: Optional[int], row, col, cell_type: CellType):
        self.x = x
        self.y = y
        self.value = value
        self.options = []
        self.row = row
        self.col = col
        self.cell_type = cell_type


class Group:
    def __init__(self, cells: list, direction: Direction, anchor: Cell, total: int):
        self.cells = cells
        self.direction = direction
        self.anchor = anchor
        self.total = total
        self.len = 0

    def add_cell(self, cell: Cell):
        self.cells.append(cell)
        self.len += 1
