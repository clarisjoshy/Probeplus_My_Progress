#Sample for using pytest markers

import pytest

@pytest.mark.addition
def test_addition():
    assert 1 + 1 == 2                #test pass

@pytest.mark.addition
def test_addition_negative_numbers():
    assert 3 + (-2) == 3              #test fails

@pytest.mark.subtraction
def test_subtraction():
    assert 5 - 3 == 2               #test pass

@pytest.mark.multiplication
def test_multiplication():
    assert 2 * 3 == 6                #test fails
    
#Run 'pytest -m addition' to run functions having marker as addition

