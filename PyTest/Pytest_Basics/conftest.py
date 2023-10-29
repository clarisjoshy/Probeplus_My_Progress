""" conftest.py is a special configuration file that allows you to define fixtures
and other configurations that can be shared across multiple test files."""
#Can be used for defining pytest fixtures

#Suppose we are having pytest files that making use of the fixture defined in conftest.py..
# The tests will look for fixture in the same file. As the fixture is not found in the file, it will check for fixture in conftest.py file.
# On finding it, the fixture method is invoked and the result is returned to the input argument of the test


import pytest

@pytest.fixture
def input_value():
   input = 10
   return input

@pytest.fixture
def test_user():
    return {"username": "testuser", "email": "testuser@example.com"}