import requests

url_base = "http://pokeapi.co/api/v2/pokemon/1/"

print(requests.get(url_base).text)
