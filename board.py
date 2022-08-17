from cell import Cell
from group import Group


class Board:
    def __init__(self, groups: list, cells: list, height: int, width: int):
        self.groups = groups
        self.cells = cells
        self.height = height
        self.width = width

