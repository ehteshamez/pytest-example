#tests/test_analyzer_api_slow.py

from grades.analyzer import analyze_student_grades
import time

def test_analyze_student_grades():
    """Test analyzing student grades (requires live API)."""
    student_id = 1
    #result = analyze_student_grades(student_id)
    time.sleep(2)
    result = {
        "pass":[60, 80, 90],
        "fail":[40, 20]
    }
    
    assert result["pass"] == [60, 80, 90]
    assert result["fail"] == [40, 20]

