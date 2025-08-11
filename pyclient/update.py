import requests

number = int(input('number: '))
endponit = f'http://localhost:8000/api/accounts/{number}/update/'
data ={
    'category_type': 'student',
    'actif': False,
}
response = requests.put(endponit,data=data)


print(response.status_code)
print(response.json())
