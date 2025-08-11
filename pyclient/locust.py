from locust import HttpUser, task, between

class MyApiUser(HttpUser):
    wait_time = between(1, 5)  # seconds between requests

    @task
    def get_items(self):
        self.client.get('http://localhost:8000/api/accounts/')  # adjust to your DRF endpoint

    @task
    def create_item(self):
        self.client.post('http://localhost:8000/api/accounts/create/', json={"category_type": "teacher", "actif": True})