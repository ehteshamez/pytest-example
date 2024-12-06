#tests/conftest.py
import pytest

@pytest.fixture
def mixed_grades():
    return [40, 60, 80, 20, 90]

@pytest.fixture
def all_passing_grades():
    return [55, 70, 85, 95]

@pytest.fixture
def all_failing_grades():
    return [30, 20, 40, 45]

@pytest.fixture
def empty_grades():
    return []
