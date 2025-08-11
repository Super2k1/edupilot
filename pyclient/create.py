import requests


endpoint = 'http://localhost:8000/api/accounts/create/'
data = {
    'category_type': 'student',
    'actif': True,}
response = requests.post(endpoint, json=data)

print(response.status_code)
print(response.json())