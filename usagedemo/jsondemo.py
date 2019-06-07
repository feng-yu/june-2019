"""
Demo the basic usage for json package

"""
import json
import requests
from datetime import datetime


url = 'http://openexchangerates.org/api/latest.json'
payload = {'app_id':'d7d7c7e65baf4c6b96a05d39e7085efd'}

res = requests.get(url, params=payload)
print(res.url)

if res.status_code == 200:
    data = res.json()

    with open('openexchange.json', 'w') as f:
        json.dump(data, f, indent=2)

    date = datetime.fromtimestamp(data['timestamp'])
    base = data['base']
    rates = data['rates']
    cny_rate = rates['CNY']

    print(date)
    print(base)
    print(cny_rate)

