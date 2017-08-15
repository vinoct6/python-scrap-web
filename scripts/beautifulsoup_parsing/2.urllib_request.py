url = "http://127.0.0.1:8001"

import urllib.request

request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
html = response.read()
print(html)
