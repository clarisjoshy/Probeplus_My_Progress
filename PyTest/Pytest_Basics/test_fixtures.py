# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are useful for setting up common data or resources that multiple test functions can use,
# making your test code more organized 

import pytest

# Define a simple fixture to create a sample list
@pytest.fixture
def list_num():
    return [1, 2, 3, 4, 5]

# Test function that uses the 'list_num' fixture
def test_list_contains_element(list_num):
    assert 3 in list_num             #Test will pass

# Another test function using the 'list_num' fixture
def test_list_has_length(list_num):
    assert len(list_num) == 4        #Test will fail as length is 5
