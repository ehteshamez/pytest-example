def categorize_grades(grades):
    """Categorize grades into pass and fail lists."""
    pass_grades = [g for g in grades if g >= 50]
    fail_grades = [g for g in grades if g < 50]
    return {"pass": pass_grades, "fail": fail_grades}
