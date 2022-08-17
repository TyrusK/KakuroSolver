from group import Group

class Cell:
    def __init__(self, x: int, y: int, value: int, row: Group, col: Group):
        self.x = x
        self.y = y
        self.value = value
        self.options = []
        self.row = row
        self.col = col
