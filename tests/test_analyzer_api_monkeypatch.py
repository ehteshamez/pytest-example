# tests/test_analyzer_api_monkeypatch.py
import pytest
from grades.analyzer import analyze_student_grades

def test_analyze_student_grades_with_monkeypatch(monkeypatch):
    """Test analyzing student grades using a mocked API call."""

    # Define the mock function
    def mock_fetch_grades(student_id):
        return [40, 60, 80, 20, 90]

    # Patch the fetch_grades function as it is used in analyzer
    monkeypatch.setattr("grades.analyzer.fetch_grades", mock_fetch_grades)

    # Call the function under test
    student_id = 1
    result = analyze_student_grades(student_id)

    # Assertions
    assert result["pass"] == [60, 80, 90]
    assert result["fail"] == [40, 20]
