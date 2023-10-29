import pytest
import requests
from urllib.parse import urljoin
def get_user_token():           #A sample function for getting token
    token="ABSJNWOIDJWIJSOIWs123dwid"
    return token


base_url = "http://localhost:8000"
pytestmark = pytest.mark.book
timeout = 5

class TestGetBookAPI:
    """Testcases of get_book API"""

    @classmethod
    def setup_class(cls):
        """Function to set up the data required before running pytests"""
        cls.get_url = urljoin(base_url, "get_book")

    @pytest.mark.parametrize(
        "book_id", [
            "invalid_id_1",
            "invalid_id_2"
        ]
    )
    def test_invalid_book_id(cls, book_id):
        """Test to get a book with an invalid book id"""
        url = urljoin(cls.get_url+'/', book_id)
        token = get_user_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url=url,headers=headers ,timeout=timeout)
        assert response.status_code == 404                     

    def test_valid_book_id(cls):
        """Test to get a book with a valid book id"""
        book_id = "BK910"           #for eg:valid book id
        url = urljoin(cls.get_url+'/', book_id)
        token = get_user_token()
        headers = {"Authorization": f"Bearer {token}"}
        response = requests.get(url=url, headers=headers ,timeout=timeout)
        assert response.status_code == 200
