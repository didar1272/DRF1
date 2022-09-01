import requests

endpoint = "http://localhost:8000/api/products/list_create/"

data = {
    "title": "List create api view",
    "price": 40.00
}

# get_response = requests.post(endpoint, json=data)
get_response = requests.get(endpoint)

print(get_response.json())

