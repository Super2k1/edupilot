import requests

number = int(input('number: '))

try:
    number = int(number)
except ValueError:
    number = None
    print(f'Error: "{number}" is not a valid number.')
if number:    
    endponit = f'http://localhost:8000/api/accounts/{number}/delete/'

    response = requests.delete(endponit)


    print(response.status_code)
