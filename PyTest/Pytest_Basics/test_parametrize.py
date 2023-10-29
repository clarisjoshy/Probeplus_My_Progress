import pytest

# Define a function that performs the actual test
def add(a, b):
    return a + b

# Define the test function and use the @pytest.mark.parametrize decorator
@pytest.mark.parametrize("a, b, expected_result", [
    (1, 2, 3),      # Test case 1
    (5, 5, 10),     # Test case 2
    (0, 0, 0),      # Test case 3
    (-1, 1, 0),     # Test case 4
])

def test_addition(a, b, expected_result):
    result = add(a, b)
    assert result == expected_result

# When you run this test, pytest will run it for all parameter sets defined above.
