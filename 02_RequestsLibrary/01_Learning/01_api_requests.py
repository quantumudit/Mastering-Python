import requests

baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

r = requests.get(baseurl + endpoint)

data = r.json()

pages = data['info']['pages']

name = data['results'][0]['name']
episodes = data['results'][0]['episode']

print(len(episodes))