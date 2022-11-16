from tkinter import BOTH

from cellType import CellType
from direction import Direction
from display import Display
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
        self.square_size = None

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

    """def draw(self):

        self.canvas.pack(fill=BOTH, expand=1)

        square_size = self.square_size
        width = square_size * self.width + 9
        height = square_size * self.height + 9

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
                    self.canvas.create_rectangle(4 + square_size * x, 4 + square_size * y, 4 + square_size * (x + 1),
                                                 4 + square_size * (y + 1), width=0, fill="#7DC586")
                    self.canvas.create_line(4 + square_size * x, 4 + square_size * y, 4 + square_size * (x + 1),
                                            4 + square_size * (y + 1), width=square_size * 3 / 80)
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.VERTICAL:
                        font_size = int(square_size / 4)
                        self.canvas.create_text(4 + square_size * (x + 0.5), 4 + square_size * (y + 0.85),
                                                text=str(group.total), fill="black", font=f'Helvetica {font_size} bold')
                        group_num += 1
                        if group_num < max_group:
                            group = self.groups[group_num]
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.HORIZONTAL:
                        shift_percent = 0.81
                        if group.total < 10:
                            shift_percent = 0.89
                        font_size = int(square_size / 4)
                        self.canvas.create_text(4 + square_size * (x + shift_percent), 4 + square_size * (y + 0.5),
                                                text=str(group.total), fill="black", font=f'Helvetica {font_size} bold')
                        group_num += 1
                else:
                    cell.draw()
                x += 1
                if x > self.width - 1:
                    x = 0
            y += 1

        line_width = round(square_size * 3 / 80)
        # print(f"line width: {line_width}")
        for i in range(self.width + 1):
            self.canvas.create_line(4 + square_size * i, 4, 4 + square_size * i, height - 5, width=line_width)

        for i in range(self.height + 1):
            self.canvas.create_line(4, 4 + square_size * i, width - 5, 4 + square_size * i, width=line_width)

        self.canvas.create_rectangle(4, 4, 4 + self.width * square_size, 4 + self.width * square_size, width=line_width)

        return"""

    # Next step is try dif algorithm where group removes don't call cell removes, go over board many times
    '''def fill_cell_options3(self):
        for group in self.groups:
            group.find_sum_options(group.total, group.size, group.size, [])
        for cell_line in self.cells:
            for cell in cell_line:
                if cell.cell_type == CellType.SPACE:
                    # print(f"Starting cell ({cell.x}, {cell.y})")
                    cell.find_options3()'''

    def fill_cell_options(self, display: Display):
        for group in self.groups:
            group.find_sum_options(group.total, group.size, group.size, [])
        done = False
        while not done:
            done = True
            for cell_line in self.cells:
                for cell in cell_line:
                    if cell.cell_type == CellType.SPACE:
                        # print(f"Starting cell ({cell.x}, {cell.y})")
                        if cell.find_options(display):
                            done = False

    def finish_board(self):
        target_num_options = 2
        while True:
            print(f"Target: {target_num_options}")
            found_value = False
            for line in self.cells:
                for cell in line:
                    if cell.cell_type == CellType.SPACE and len(cell.options) == target_num_options:
                        found_value = cell.try_removing_options()
                        if found_value:
                            break
                if found_value:
                    break
            if found_value:
                target_num_options = 2
                continue
            if target_num_options == 9:
                break
            target_num_options += 1
