import requests
from getpass import getpass

def get_token():
    auth_endpoint = 'http://localhost:8000/api/auth/'
    username = input('Username: ')
    password = getpass('Password: ')
    
    auth_response = requests.post(auth_endpoint, json={
        'username': username,
        'password': password
    })
    
    if auth_response.status_code == 200:
        return auth_response.json().get('token')
    return None

def create_account(token):
    endpoint = 'http://localhost:8000/api/accounts/create/'
    headers = {
        'Authorization': f'Token {token}',  # Changed from 'bearer' to 'Token'
        'Content-Type': 'application/json'
    }
    
    data = {
        'category_type': 'student',
        'actif': True,
    }
    
    return requests.post(endpoint, json=data, headers=headers)

def main():
    token = get_token()
    if not token:
        print("Authentication failed")
        return
        
    try:
        response = create_account(token)
        response.raise_for_status()
        print(f"Status Code: {response.status_code}")
        print("Response:", response.json())
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        print(f"Response text: {response.text}")

if __name__ == "__main__":
    main()