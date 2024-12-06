import pytest
from grades.calculator import average

# Basic test
def test_average():
    grades = [70, 80, 90]
    assert average(grades) == 80

# Testing an edge case
def test_average_empty_list():
    with pytest.raises(ValueError, match="Grades list cannot be empty."):
        average([])
