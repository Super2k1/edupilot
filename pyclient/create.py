import requests


endpoint = 'http://localhost:8000/api/accounts/create/'
data = {
    'category_type': 'student',
    'actif': True,}
try:
    response = requests.post(endpoint, json=data)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    print(response.status_code)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    print(f"Response text: {response.text}")