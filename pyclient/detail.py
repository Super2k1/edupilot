import requests

number = int(input('number: '))
endponit = f'http://localhost:8000/api/accounts/{number}/'

response = requests.get(endponit)


print(response.status_code)
print(response.json())
