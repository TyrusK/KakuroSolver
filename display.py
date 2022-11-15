from tkinter import BOTH

from cellType import CellType
from direction import Direction


class Display:

    def __init__(self, canvas, root):
        self.canvas = canvas
        self.root = root

    def draw_board(self, board):
        self.canvas.pack(fill=BOTH, expand=1)

        square_size = board.square_size
        width = square_size * board.width + 9
        height = square_size * board.height + 9

        if len(board.groups) == 0:
            return
        x = 0
        y = 0
        group_num = 0
        max_group = len(board.groups)
        group = board.groups[group_num]
        for line in board.cells:
            for cell in line:
                if group_num < max_group:
                    group = board.groups[group_num]
                if cell.cell_type == CellType.WALL:
                    self.canvas.create_rectangle(4 + square_size * x, 4 + square_size * y, 4 + square_size * (x + 1),
                                                 4 + square_size * (y + 1), width=0, fill="#7DC586")
                    self.canvas.create_line(4 + square_size * x, 4 + square_size * y, 4 + square_size * (x + 1),
                                            4 + square_size * (y + 1), width=square_size * 3 / 80)
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.VERTICAL:
                        font_size = int(square_size / 4)
                        self.canvas.create_text(4 + square_size * (x + 0.5), 4 + square_size * (y + 0.85),
                                                text=str(group.total), fill="black",
                                                font=f'Helvetica {font_size} bold')
                        group_num += 1
                        if group_num < max_group:
                            group = board.groups[group_num]
                    if group.anchor.x == x and group.anchor.y == y and group.direction == Direction.HORIZONTAL:
                        shift_percent = 0.81
                        if group.total < 10:
                            shift_percent = 0.89
                        font_size = int(square_size / 4)
                        self.canvas.create_text(4 + square_size * (x + shift_percent), 4 + square_size * (y + 0.5),
                                                text=str(group.total), fill="black",
                                                font=f'Helvetica {font_size} bold')
                        group_num += 1
                else:
                    self.draw_cell(cell)
                x += 1
                if x > board.width - 1:
                    x = 0
            y += 1

        line_width = round(square_size * 3 / 80)
        # print(f"line width: {line_width}")
        for i in range(board.width + 1):
            self.canvas.create_line(4 + square_size * i, 4, 4 + square_size * i, height - 5, width=line_width)

        for i in range(board.height + 1):
            self.canvas.create_line(4, 4 + square_size * i, width - 5, 4 + square_size * i, width=line_width)

        self.canvas.create_rectangle(4, 4, 4 + board.width * square_size, 4 + board.width * square_size,
                                     width=line_width)

        return

    def draw_cell(self, cell):
        square_size = cell.board.square_size
        edge_space = 0.2
        self.canvas.create_rectangle(4 + square_size * (cell.x + 1.5 * edge_space - 0.25),
                                     4 + square_size * (cell.y + 1.5 * edge_space - 0.25),
                                     4 + square_size * (cell.x - 1.5 * edge_space + 1.25),
                                     4 + square_size * (cell.y - 1.5 * edge_space + 1.25),
                                     width=0, fill="white")
        if cell.value is None and len(cell.options) == 1:
            cell.value = cell.options.pop()
            cell.options.add(cell.value)
        if cell.value is None or len(cell.options) == 0:
            font_size = int(square_size / 4)
            for num in range(1, 10):
                cell_x = 4 + square_size * (cell.x + edge_space + ((num - 1) % 3) * (0.5 - edge_space))
                cell_y = 4 + square_size * (cell.y + edge_space + round((num - 2) / 3) * (0.5 - edge_space))
                if num in cell.options:
                    self.canvas.create_text(cell_x, cell_y, text=str(num), fill="black", font=f'Helvetica {font_size}')
        else:
            font_size = int(square_size * 5 / 8)
            self.canvas.create_text(4 + square_size * (cell.x + 0.5), 4 + square_size * (cell.y + 0.5),
                                    text=str(cell.value), fill="black", font=f'Helvetica {font_size}')
