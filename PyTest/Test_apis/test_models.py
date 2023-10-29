import pytest
from pydantic import ValidationError

class CreateBook:
    name: str
    weight: int

class TestCreateBook:
    def test_book(self):
        """
        Test to check if book name and weight are of invalid format
        """
        data = {}
        data['name'] = 'Harry Potter'
        data['weight'] = '400g'
        with pytest.raises(ValidationError):
            CreateBook(**data)
