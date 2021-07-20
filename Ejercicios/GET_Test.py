import requests

url = "http://httpbin.org/get"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)