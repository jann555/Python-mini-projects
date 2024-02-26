import os
from datetime import datetime
from dotenv import load_dotenv
import requests

load_dotenv()
USERNAME = os.getenv('USERNAME')
TOKEN = os.getenv('TOKEN')
pixela_endpoint = 'https://pixe.la/v1/users'
GRAPH_ID = 'graph1'

user_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_config = {
    'id': GRAPH_ID,
    'name': 'Study Graph',
    'unit': 'hrs',
    'type': 'float',
    'color': 'sora'
}
headers = {
    'X-USER-TOKEN': TOKEN
}
# https://pixe.la/v1/users/jannick/graphs/graph1.html
# response_p = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response_p.text)

pixel_endpoint = f'{pixela_endpoint}/{USERNAME}/{GRAPH_ID}'

today = datetime.now().strftime('%Y%m%d')

pixel_data = {
    'date': today,
    'quantity': '2.5',
}

# response_post_p = requests.post(url=pixel_endpoint, headers=headers, json=pixel_data)
# print(response_post_p.text)
pixel_endpoint_update = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'
pixel_update = {
    'quantity': '2.77',
}
# r = requests.put(url=pixel_endpoint_update, headers=headers, json=pixel_update)
# print(r.text)

pixel_endpoint_delete = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}'

r = requests.delete(url=pixel_endpoint_update, headers=headers)
print(r.text)
