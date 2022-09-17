from direction import Direction
from cellType import CellType
from typing import Optional


class Cell:
    def __init__(self, x: int, y: int, value: Optional[int], cell_type: CellType):
        self.x = x
        self.y = y
        self.value = value
        self.options = []
        self.row = None
        self.col = None
        self.row_index = None
        self.col_index = None
        self.cell_type = cell_type
        self.options = set()

    def find_options(self):
        group = self.row
        index = self.row_index
        while True:
            option_list = set()
            for sum_option in group.sum_options:
                option_list.add(sum_option[index])
            if group == self.row:
                self.options = option_list
            else:
                # temp solution
                self.options = self.options.intersection(option_list)

                """
                # remove nums with special method that calls group method that calls it etc
                temp_set = self.options.copy()
                for num in temp_set:
                    if not num in option_list:
                        self.remove_num_option(num)
                """

                break
            group = self.col
            index = self.col_index


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
            sum_option.append(num)
            if len(sum_option) == true_size:
                new_sum_option = sum_option.copy()
                self.sum_options.append(new_sum_option)
                del sum_option[-1]
                return
            else:
                self.find_sum_options(total - num, size - 1, true_size, sum_option)
            del sum_option[-1]
