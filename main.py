import requests

url = xxx
resp = requests.get(url, headers=headers, data=data)
print(resp.text)

print("username:admin")
