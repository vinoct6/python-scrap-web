import requests

url = "http://127.0.0.1:8001"
response = requests.get(url)
html = response.text

print(html)



