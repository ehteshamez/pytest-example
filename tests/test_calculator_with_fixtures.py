import pytest
from grades.calculator import average

# Basic test
def test_average(mixed_grades):
    assert average(mixed_grades) == 58

# Testing an edge case
def test_average_empty_list(empty_grades):
    with pytest.raises(ValueError, match="Grades list cannot be empty."):
        average(empty_grades)
