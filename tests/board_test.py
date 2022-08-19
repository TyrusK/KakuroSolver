import pytest
from board_str import board_str
from reader import reader


def test_board_string():
    board = reader("test_file.txt")
    old_string = ""
    with open("test_file.txt", "r") as file:
        line = file.readline()
        while line != "":
            old_string += line
            line = file.readline()
    new_string = board_str(board)

    assert old_string == new_string
