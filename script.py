import json
import requests

url = "http://57.128.166.240/trip-order/promo"

with open("data.json") as f:
    data = json.load(f)

# post to url
response = requests.post(url=url, json=data)
print(response.status_code)