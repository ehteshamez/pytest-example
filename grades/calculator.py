def average(grades):
    """Calculate the average of a list of grades."""
    if not grades:
        raise ValueError("Grades list cannot be empty.")
    return sum(grades) / len(grades)
