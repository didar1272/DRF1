import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, data={"query": "Hello World"}) # HTTP request

print(get_response.text) #print raw response

print(get_response.json())