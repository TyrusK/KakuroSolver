from cell import Cell
from direction import Direction


class Group:
    def __init__(self, cells: list, direction: Direction, anchor: Cell, total: int):
        self.cells = cells
        self.direction = direction
        self.anchor = anchor
        self.total = total
