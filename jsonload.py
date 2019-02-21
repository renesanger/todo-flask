import json
from pprint import pprint

with open('data.json') as file:
	data = file.load()

pprint(data)

