# requests para requisições HTTP
# Tutorial -> https://youtu.be/Qd8JT0bnJGs
import requests

# http:// -> 80
# https:// -> 443
url = 'http://localhost:5500'
response = requests.get(url)

print(response.status_code)
# print(response.headers)
# print(response.content)
print(response.text)
