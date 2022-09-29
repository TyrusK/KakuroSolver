import time

from direction import Direction
from cellType import CellType
from typing import Optional

class Cell:
    def __init__(self,x: int, y: int, value: Optional[int], cell_type: CellType):
        self.board = None
        self.x = x
        self.y = y
        self.value = value
        self.options = []
        self.row = None
        self.col = None
        self.row_index = None
        self.col_index = None
        self.cell_type = cell_type
        self.options = set(range(1, 10))

    def remove_num_option(self, num: int):
        self.options.remove(num)
        self.draw()
        self.board.root.update()
        time.sleep(1)
        group = self.row
        index = self.row_index
        while True:
            temp_sum_options = group.sum_options.copy()
            for sum_option in temp_sum_options:
                if sum_option[index] == num and sum_option in group.sum_options:
                    group.remove_sum_option(sum_option)
            if group == self.col:
                break
            group = self.col
            index = self.col_index

    def find_options(self):
        row_options = set()
        group = self.row
        index = self.row_index
        while True:
            col_options = set()
            for sum_option in group.sum_options:
                col_options.add(sum_option[index])
            if group == self.row:
                row_options = col_options
            else:
                # remove nums with special method that calls group method that calls it etc
                # This should call for nums that are in only the row or only the col
                temp_set = self.options.copy()
                for num in temp_set:
                    if num not in row_options or num not in col_options:
                        self.remove_num_option(num)

                break
            group = self.col
            index = self.col_index

    def draw(self):
        edge_space = 0.2
        square_size = self.board.square_size
        font_size = int(square_size / 4)
        self.board.canvas.create_rectangle(4 + square_size * (self.x + 1.5 * edge_space - 0.25),
                                           4 + square_size * (self.y + 1.5 * edge_space - 0.25),
                                           4 + square_size * (self.x - 1.5 * edge_space + 1.25),
                                           4 + square_size * (self.y - 1.5 * edge_space + 1.25),
                                           width=0, fill="white")
        for num in range(1,10):
            cell_x = 4 + square_size * (self.x + edge_space + ((num - 1) % 3) * (0.5 - edge_space))
            cell_y = 4 + square_size * (self.y + edge_space + round((num - 2) / 3) * (0.5 - edge_space))
            if num in self.options:
                self.board.canvas.create_text(cell_x, cell_y, text=str(num), fill="black",font=f'Helvetica {font_size}')


def sum_list(int_list: list):
    total = 0
    for num in int_list:
        total += num
    return total


class Group:
    def __init__(self, cells: list, direction: Direction, anchor: Cell, total: int):
        self.cells = cells
        self.direction = direction
        self.anchor = anchor
        self.total = total
        self.size = 0
        self.sum_options = []

    def add_cell(self, cell: Cell):
        self.cells.append(cell)
        self.size += 1

    def find_sum_options(self, total: int, size: int, true_size: int, sum_option: list):
        min_value = max(total - (20 - size) * (size - 1) * 0.5, 1)
        max_value = min(total - size * (size - 1) * 0.5, 9)
        for num in range(int(min_value), int(max_value + 1)):
            if num in sum_option:
                continue
            cell = self.cells[len(sum_option)]
            if cell.value is not None and cell.value != num:
                continue
            sum_option.append(num)
            if len(sum_option) == true_size:
                new_sum_option = sum_option.copy()
                self.sum_options.append(new_sum_option)
                del sum_option[-1]
                return
            else:
                self.find_sum_options(total - num, size - 1, true_size, sum_option)
            del sum_option[-1]

    # inefficient, maybe find new cell possibilities for all cells first then compare, reference stuff a lot less
    def remove_sum_option(self, removed_option: list):
        self.sum_options.remove(removed_option)
        i = 0
        for cell in self.cells:
            num = removed_option[i]

            found_num = False
            for sum_option in self.sum_options:
                if sum_option[i] == num:
                    found_num = True

            if num in cell.options and not found_num:
                cell.remove_num_option(num)

            i += 1
