#grades/analyzer.py
from grades.api_client import fetch_grades

def categorize_grades(grades):
    """Categorize grades into pass and fail lists."""
    pass_grades = [g for g in grades if g >= 50]
    fail_grades = [g for g in grades if g < 50]
    return {"pass": pass_grades, "fail": fail_grades}

def analyze_student_grades(student_id):
    """Fetch and categorize grades for a student."""
    grades = fetch_grades(student_id)
    pass_grades = [g for g in grades if g >= 50]
    fail_grades = [g for g in grades if g < 50]
    return {"pass": pass_grades, "fail": fail_grades}
