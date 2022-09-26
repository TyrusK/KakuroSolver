from tkinter import BOTH

from cellType import CellType
from direction import Direction
from group import Group


def num_string(group: Group):
    num = group.total
    direction = group.direction
    if num > 9:
        return str(num)
    if direction == Direction.VERTICAL:
        return f" {str(num)}"
    return f"{str(num)} "


class Board:
    def __init__(self, groups: list, cells: list, height: int, width: int):
        self.groups = groups
        self.cells = cells
        self.height = height
        self.width = width

    def __str__(self):
        string = ""
        if len(self.groups) == 0:
            return string
        x = 0
        y = 0
        group_num = 0
        max_group = len(self.groups)
        group = self.groups[group_num]
        for line in self.cells:
            for cell in line:
                if group_num < max_group:
                    group = self.groups[group_num]
                if cell.cell_type == CellType.WALL:
                    string += "|"
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.VERTICAL:
                        string += f"{num_string(group)}"
                        group_num += 1
                        if group_num < max_group:
                            group = self.groups[group_num]
                    else:
                        string += " -"
                    string += "\\"
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.HORIZONTAL:
                        string += f"{num_string(group)}"
                        group_num += 1
                    else:
                        string += "- "
                elif cell.value is not None:
                    string += f"|  {cell.value}  "
                else:
                    string += "|  .  "
                x += 1
                if x > self.width - 1:
                    string += "|\n"
                    x = 0
            y += 1
        return string

    def draw(self, canvas, square_size: int, width: int, height: int):

        canvas.pack(fill=BOTH, expand=1)

        for i in range(self.width + 1):
            canvas.create_line(4 + square_size * i, 2, 4 + square_size * i, height - 3, width=3)

        for i in range(self.height + 1):
            canvas.create_line(2, 4 + square_size * i, width - 3, 4 + square_size * i, width=3)

        if len(self.groups) == 0:
            return
        x = 0
        y = 0
        group_num = 0
        max_group = len(self.groups)
        group = self.groups[group_num]
        for line in self.cells:
            for cell in line:
                if group_num < max_group:
                    group = self.groups[group_num]
                if cell.cell_type == CellType.WALL:
                    canvas.create_rectangle(6 + square_size * x, 6 + square_size * y, 3 + square_size * (x + 1),
                                            3 + square_size * (y + 1), width=0, fill="#7DC586")
                    canvas.create_line(4 + square_size * x, 4 + square_size * y, 4 + square_size * (x + 1), 
                                       4 + square_size * (y + 1), width=3)
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.VERTICAL:
                        font_size = int(square_size / 4)
                        canvas.create_text(4 + square_size * (x + 0.5), 4 + square_size * (y + 0.85),
                                           text=str(group.total), fill="black", font=f'Helvetica {font_size} bold')
                        group_num += 1
                        if group_num < max_group:
                            group = self.groups[group_num]
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.HORIZONTAL:
                        shift_percent = 0.81
                        if group.total < 10:
                            shift_percent = 0.89
                        font_size = int(square_size / 4)
                        canvas.create_text(4 + square_size * (x + shift_percent), 4 + square_size * (y + 0.5),
                                           text=str(group.total), fill="black", font=f'Helvetica {font_size} bold')
                        group_num += 1
                elif cell.value is not None:
                    font_size = int(square_size * 5 / 8)
                    canvas.create_text(4 + square_size * (x + 0.5), 4 + square_size * (y + 0.5), text=str(cell.value),
                                       fill="black", font=f'Helvetica {font_size}')
                else:
                    edge_space = 0.2
                    for num in range(1, 10):
                        if num in cell.options:
                            canvas.create_text(4 + square_size * (x + edge_space + ((num - 1) % 3) * (0.5 - edge_space)),
                                               4 + square_size * (y + edge_space + round((num - 2) / 3) * (0.5 - edge_space)),
                                               text=str(num), fill="black", font='Helvetica 20')
                x += 1
                if x > self.width - 1:
                    # string += "|\n"
                    x = 0
            y += 1
        return

    def fill_cell_options(self):
        for group in self.groups:
            group.find_sum_options(group.total, group.size, group.size, [])
        for cell_line in self.cells:
            for cell in cell_line:
                if cell.cell_type == CellType.SPACE:
                    print(f"Starting cell ({cell.x}, {cell.y})")
                    cell.find_options()
                    print(f"Finished cell ({cell.x}, {cell.y})")

    def find_values(self):
        for cell_line in self.cells:
            for cell in cell_line:
                if cell.cell_type == CellType.SPACE and len(cell.options) == 1:
                    cell.value = cell.options.pop()
