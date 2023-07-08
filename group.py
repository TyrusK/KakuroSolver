import copy
import time

import display
from direction import Direction
from cellType import CellType
from typing import Optional


# Can I remove value?
from display import Display


class Cell:
    def __init__(self, x: int, y: int, value: Optional[int], cell_type: CellType):
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

    # The direction argument is the direction of the group calling this, so only check the other group
    # Returns false if an error was found, true if no problems
    def remove_num_option_recursive(self, num: int, direction: Optional[Direction], display: Display):
        self.options.remove(num)
        display.draw_cell(self)
        display.root.update()
        time.sleep(0.1)
        if len(self.options) == 0:
            print(f"({self.x}, {self.y}): no cell options")
            return False
        group = self.row
        index = self.row_index
        if direction == Direction.HORIZONTAL:
            group = self.col
            index = self.col_index
        while True:
            temp_sum_options = group.sum_options.copy()
            for sum_option in temp_sum_options:
                # PROBLEM: Slow?
                if sum_option[index] == num and sum_option in group.sum_options:
                    if not group.remove_sum_option_recursive(sum_option, display):
                        return False
            if group.direction == Direction.VERTICAL or direction == Direction.VERTICAL:
                break
            group = self.col
            index = self.col_index
        return True

    def remove_num_option(self, num: int, direction: Optional[Direction], display: Display):
        self.options.remove(num)
        display.draw_cell(self)
        display.root.update()
        # time.sleep(0.1)
        if len(self.options) == 0:
            print("Empty cell")
            exit()
        group = self.row
        index = self.row_index
        if direction == Direction.HORIZONTAL:
            group = self.col
            index = self.col_index
        while True:
            temp_sum_options = group.sum_options.copy()
            for sum_option in temp_sum_options:
                # PROBLEM: Slow?
                if sum_option[index] == num and sum_option in group.sum_options:
                    group.sum_options.remove(sum_option)
            if group.direction == Direction.VERTICAL or direction == Direction.VERTICAL:
                break
            group = self.col
            index = self.col_index

    def find_options_recursive(self):
        row_options = set()
        group = self.row
        index = self.row_index
        while True:
            col_options = set()
            for sum_option in group.sum_options:
                col_options.add(sum_option[index])
            if group.direction == Direction.HORIZONTAL:
                row_options = col_options
            else:
                # remove nums with special method that calls group method that calls it etc
                # This should call for nums that are in only the row or only the col
                i = 0
                temp_set = self.options.copy()
                for num in temp_set:
                    # This works because if removing one num removes another from the same cell, the second num required
                    # the first to work which is a contradiction
                    """if len(self.options) != len(temp_set) - i:
                        print("This board cannot be solved")
                        exit()"""
                    if num not in row_options or num not in col_options:
                        self.remove_num_option_recursive(num, None)
                        i += 1

                break
            group = self.col
            index = self.col_index

    def find_options(self, display: Display):
        row_options = set()
        made_changes = False
        group = self.row
        index = self.row_index
        while True:
            col_options = set()
            for sum_option in group.sum_options:
                col_options.add(sum_option[index])
            if group.direction == Direction.HORIZONTAL:
                row_options = col_options
            else:
                # remove nums with special method that calls group method that calls it etc
                # This should call for nums that are in only the row or only the col
                i = 0
                temp_set = self.options.copy()
                for num in temp_set:
                    # This works because if removing one num removes another from the same cell, the second num required
                    # the first to work which is a contradiction
                    """if len(self.options) != len(temp_set) - i:
                        print("This board cannot be solved")
                        exit()"""
                    if num not in row_options or num not in col_options:
                        made_changes = True
                        self.remove_num_option(num, None, display)
                        i += 1

                break
            group = self.col
            index = self.col_index
        return made_changes

    """def draw(self):
        square_size = self.board.square_size
        edge_space = 0.2
        self.board.canvas.create_rectangle(4 + square_size * (self.x + 1.5 * edge_space - 0.25),
                                           4 + square_size * (self.y + 1.5 * edge_space - 0.25),
                                           4 + square_size * (self.x - 1.5 * edge_space + 1.25),
                                           4 + square_size * (self.y - 1.5 * edge_space + 1.25),
                                           width=0, fill="white")
        if self.value is None and len(self.options) == 1:
            self.value = self.options.pop()
            self.options.add(self.value)
        if self.value is None or len(self.options) == 0:
            font_size = int(square_size / 4)
            for num in range(1, 10):
                cell_x = 4 + square_size * (self.x + edge_space + ((num - 1) % 3) * (0.5 - edge_space))
                cell_y = 4 + square_size * (self.y + edge_space + round((num - 2) / 3) * (0.5 - edge_space))
                if num in self.options:
                    self.board.canvas.create_text(cell_x, cell_y, text=str(num), fill="black",
                                                  font=f'Helvetica {font_size}')
        else:
            font_size = int(square_size * 5 / 8)
            self.board.canvas.create_text(4 + square_size * (self.x + 0.5), 4 + square_size * (self.y + 0.5),
                                          text=str(self.value), fill="black", font=f'Helvetica {font_size}')"""

    # return True if it made changes, False if it did not
    # Should make a new board and experiment with it for each option
    # look at removing each value, if only one gives an error the answer has been found, remove all others (if that
    # gives errors, the board is invalid)
    # if no errors from removing any option, no changes are made
    # if multiple errors, the board is invalid
    def try_removing_options(self, display: Display):
        true_value = -1
        num_errors = 0
        for option in self.options:
            # PROBLEM: this does not seem to be making a new board for each iteration
            new_board = copy.deepcopy(self.board)
            print(f"({self.x},{self.y}): {option}")
            new_cell = new_board.cells[self.y][self.x]
            if not new_cell.remove_num_option_recursive(option, None, display):
                print("error")
                num_errors += 1
                true_value = option
            else:
                print("no error")
        print(f"num_errors: {num_errors}")

        if num_errors == 0:
            return False
        if num_errors == 1:
            print(f"The value of ({self.x},{self.y}) was found to be {true_value}")
            for option in self.options:
                if option != true_value:
                    self.remove_num_option_recursive(option, None, display)
            return True
        print("This board is invalid.")
        exit()


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

    # Returns false if an error was found, true if no problems
    def remove_sum_option_recursive(self, removed_option: list, display: Display):
        sum_options = self.sum_options
        sum_options.remove(removed_option)
        i = 0
        for cell in self.cells:
            num = removed_option[i]

            # Problem: Slow? Maybe do outside loop
            found_num = False
            for sum_option in sum_options:
                if sum_option[i] == num:
                    found_num = True

            if num in cell.options and not found_num:
                if not cell.remove_num_option_recursive(num, self.direction, display):
                    return False

            i += 1
        return True
    def remove_sum_option(self, removed_option: list):
        sum_options = self.sum_options
        sum_options.remove(removed_option)
        i = 0
        for cell in self.cells:
            num = removed_option[i]

            found_num = False
            for sum_option in sum_options:
                if sum_option[i] == num:
                    found_num = True

            if num in cell.options and not found_num:
                cell.remove_num_option(num, self.direction)

            i += 1
