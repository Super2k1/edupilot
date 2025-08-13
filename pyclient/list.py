import requests
from getpass import getpass
import json

def pretty_print_json(data):
    print(json.dumps(data, indent=4))

def get_accounts(token):
    endpoint = 'http://localhost:8000/api/accounts/'
    headers = {
        'Authorization': f'Token {token}',
        'Content-Type': 'application/json'
    }
    
    response = requests.get(endpoint, headers=headers)
    return response

def main():
    # Get authentication
    auth_endpoint = 'http://localhost:8000/api/auth/'
    username = input('Username: ')
    password = getpass('Password: ')

    auth_response = requests.post(auth_endpoint, json={
        'username': username,
        'password': password
    })

    if auth_response.status_code == 200:
        token = auth_response.json().get('token')
        print("Authentication successful!")
        
        # Get accounts list
        response = get_accounts(token)
        print(f"\nStatus Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print("\nAccounts List:")
            pretty_print_json(data)
            print(f"\nTotal accounts: {len(data)}")
        else:
            print(f"Error accessing accounts: {response.text}")
    else:
        print(f"Authentication failed: {auth_response.text}")

if __name__ == "__main__":
    main()