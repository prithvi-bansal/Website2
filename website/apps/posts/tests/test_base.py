import pytest

def test_example():
    print("Test 1")
    assert 1 == 1

@pytest.mark.skip
def test_example1():
    print("Test 2")
    assert 1 == 1