#tests/test_markers.py

import pytest

# Skip the test
@pytest.mark.skip(reason="Not implemented yet")
def test_feature_not_ready():
    assert False  # This won't run

# Mark a test as expected to fail
@pytest.mark.xfail(reason="Known bug in version 1.0")
def test_buggy_feature():
    assert 1 == 2  # Test will run but won't fail the suite
