import requests

r = requests.get("https://bjex.ca")
print(r.status_code)
print(r.ok)
