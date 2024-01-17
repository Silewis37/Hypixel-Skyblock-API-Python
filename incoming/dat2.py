import requests
import json

def api_request(url, headers):
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('Successfully pulled data!')

        with open('levelpoints.json', 'w') as file:
            json.dump(response.json(), file, indent=4)
    else:
        print(f'Request failed. Status code: {response.status_code}')

url = 'https://api.hypixel.net/v2/resources/skyblock/skills'
headers = {'API-Key': 'e2a42c13-f139-4190-b850-6d0613e6d2fa'}

api_request(url, headers)