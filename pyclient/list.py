import requests


endpoint = 'http://localhost:8000/api/accounts/'

response = requests.get(endpoint)

lenght = len(response.json())


print(response.status_code)
print(response.json())
print(f"Number of items: {lenght}") 