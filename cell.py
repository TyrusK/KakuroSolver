from group import Group
from cellType import CellType


class Cell:
    def __init__(self, x: int, y: int, value: int, row: Group, col: Group, cell_type: CellType):
        self.x = x
        self.y = y
        self.value = value
        self.options = []
        self.row = row
        self.col = col
        self.cell_type = cell_type
