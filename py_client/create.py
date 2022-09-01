import requests

endpoint = "http://localhost:8000/api/products/create/"

data = {
    "title": "This field is done",
    "price": 40.00
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())

