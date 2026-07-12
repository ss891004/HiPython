import requests

r= requests.get("http://www.jshmrcb.com")

# print(r.text)

print(r.status_code)