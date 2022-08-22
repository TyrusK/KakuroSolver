import pytest
from reader import reader


def test_board_string():
    board = reader("../test_file.txt")
    old_string = ""
    with open("../test_file.txt", "r") as file:
        line = file.readline()
        while line != "":
            old_string += line
            line = file.readline()
    assert old_string == str(board)


def test_groups():
    board = reader("../test_file.txt")
    groups = board.groups
    assert len(groups) == 20

    sum = 0
    for group in groups:
        sum += group.total
    assert sum == 234
