import pytest
from board import Board


def test_basic():
    assert 1 == 1


def test_filename():
    f = "test_file.txt"
    b = Board(f)
    assert b
    assert b.filename == f
