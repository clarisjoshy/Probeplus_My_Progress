#Basic test functions using assert statement
import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5  ## Test will pass as the condition is satisfying
   
def test_greater():
   num = 100
   assert num > 100    ## Test will fail
   
def test_list_not_empty():
    my_list = [1, 2, 3]
    assert not len(my_list) == 0       #Test will passas it checks the condition "List should not be empty"