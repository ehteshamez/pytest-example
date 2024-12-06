#tests/test_analyzer_with_fixtures.py
import pytest
from grades.analyzer import categorize_grades


# Use fixtures in test cases
def test_categorize_grades_with_mixed_grades(mixed_grades):
    result = categorize_grades(mixed_grades)
    assert result["pass"] == [60, 80, 90]
    assert result["fail"] == [40, 20]

def test_categorize_grades_with_all_passing(all_passing_grades):
    result = categorize_grades(all_passing_grades)
    assert result["pass"] == all_passing_grades
    assert result["fail"] == []

def test_categorize_grades_with_all_failing(all_failing_grades):
    result = categorize_grades(all_failing_grades)
    assert result["pass"] == []
    assert result["fail"] == all_failing_grades

def test_categorize_grades_with_empty_list(empty_grades):
    result = categorize_grades(empty_grades)
    assert result["pass"] == []
    assert result["fail"] == []
