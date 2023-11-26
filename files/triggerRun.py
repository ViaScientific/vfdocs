import requests
import os

# Function to login and get access token
def get_access_token(email, password):
    url = 'https://www.viafoundry.com/vmeta/api/v1/users/login'
    payload = {
        "email": email,
        "password": password
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json().get('token')
    else:
        raise Exception("Login failed")

# Function to trigger a pipeline
def trigger_pipeline(access_token, run_settings):
    url = 'https://www.viafoundry.com/vpipe/api/service.php?run=startRun'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=run_settings)
    return response.json()

# Reading credentials from environment variables
email = os.getenv('VIAFOUNDRY_EMAIL')
password = os.getenv('VIAFOUNDRY_PASSWORD')

# Validate that credentials are set
if not email or not password:
    raise ValueError("Email or Password environment variables are not set")


run_settings = {
    # Add your run details here
    "doc": {
          "name": "New Run Name",
          "tmplt_id": 861,
          "in": {
                "testFile": "s3://viafoundry/run_data/test_data/models/data/AmpC_screen_table_subset_10K.csv",
                "numLine": "3000",
                "Header": "smiles"
          }
    }
}

# Login and trigger the pipeline
try:
    token = get_access_token(email, password)
    result = trigger_pipeline(token, run_settings)
    print("Pipeline triggered successfully:", result)
except Exception as e:
    print("An error occurred:", e)


