import requests
import json

url = "http://httpbin.org/post"

payload = json.dumps({
  "key1": 1,
  "key2": "value2"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

