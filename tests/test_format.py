import pytest
from reader import reader


def test_basic():
    assert 1 == 1


def test_filename():
    f = "test_file.txt"
    b = reader(f)
    assert b
    assert b.filename == f
