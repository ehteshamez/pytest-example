from grades.analyzer import categorize_grades

def test_categorize_grades_with_mixed_grades():
    grades = [40, 60, 80, 20, 90]
    result = categorize_grades(grades)
    assert result["pass"] == [60, 80, 90]
    assert result["fail"] == [40, 20]

def test_categorize_grades_with_all_passing():
    grades = [55, 70, 85, 95]
    result = categorize_grades(grades)
    assert result["pass"] == grades
    assert result["fail"] == []

def test_categorize_grades_with_all_failing():
    grades = [30, 20, 40, 45]
    result = categorize_grades(grades)
    assert result["pass"] == []
    assert result["fail"] == grades

def test_categorize_grades_with_empty_list():
    grades = []
    result = categorize_grades(grades)
    assert result["pass"] == []
    assert result["fail"] == []
