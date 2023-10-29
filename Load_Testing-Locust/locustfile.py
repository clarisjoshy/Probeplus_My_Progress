from urllib.parse import urljoin
from locust import HttpUser, task,tag
import requests
import time


base_url="http://localhost:8000"
def get_user_token():
    token="QYWHUUW122XSXSS21"
    return token

class QuickstartUser(HttpUser):
    # wait_time = between(1,3)
    
    @tag("book")
    @task
    def get_book(self):
        token=get_user_token()
        id="BK023"
        headers = {"Authorization": f"Bearer {token}","Content-Type": "application/json"}
        url=urljoin(f"{base_url}/get_book"+'/',id)
        time.sleep(2)
        self.client.get(url=url,headers=headers)
        
    @tag("book")
    @task
    def update_book(self):
        token=get_user_token()
        id="BK023"
        headers = {"Authorization": f"Bearer {token}","Content-Type": "application/json"}
        url=urljoin(f"{base_url}/update_book"+'/',id)
        time.sleep(2)
        self.client.put(url=url,headers=headers)
        
    @tag("book")
    @task
    def create_book(self):
        token=get_user_token()
        headers = {"Authorization": f"Bearer {token}","Content-Type": "application/json"}
        data={
            "id":"BK123",
            "name": "Harry Potter"
        }
        url=urljoin(f"{base_url}/create_book")
        time.sleep(2)
        self.client.post(url=url,headers=headers,json=data)