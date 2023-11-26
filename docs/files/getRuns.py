import requests
import os

# Function to login and get access token
def get_access_token(email, password):
    login_url = 'https://www.viafoundry.com/vmeta/api/v1/users/login'
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(login_url, json=payload)
    if response.status_code == 200:
        return response.json().get('token')
    else:
        raise Exception("Login failed")

# Function to get the list of runs
def get_runs(access_token):
    runs_url = 'https://www.viafoundry.com/vpipe/api/service.php?data=getRuns'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    response = requests.get(runs_url, headers=headers)
    return response.json()

# Reading credentials from environment variables
email = os.getenv('VIAFOUNDRY_EMAIL')
password = os.getenv('VIAFOUNDRY_PASSWORD')

# Validate that credentials are set
if not email or not password:
    raise ValueError("Email or Password environment variables are not set")

# Execute the process
try:
    token = get_access_token(email, password)
    runs = get_runs(token)
    print("List of Runs:", runs)
except Exception as e:
    print("An error occurred:", e)
