import requests
import json

try:
    r = requests.get('http://localhost:5000/')
    print(r.text)
    json_stuff = json.loads(r.text)
    print(json_stuff['status'])
except Exception as e:
    print(e)