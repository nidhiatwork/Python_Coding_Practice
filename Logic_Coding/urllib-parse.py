import urllib.parse


sample_url = "https://server.example.com:8080/example.html?val1=1&val2=Hello+World"

result = urllib.parse.urlparse(sample_url)
print(result)
print(result.scheme, result.hostname, result.path)
print(result.geturl())

#find values which can be safely used in urls
name = "Nidhi Bhushan~"
result = urllib.parse.quote(name)
print(result)
result = urllib.parse.quote_plus(name)
print(result)

#Using maps to put values in urls
d = {"name": "Nidhi Bhushan", "place": "Noida"}
result = urllib.parse.urlencode(d)
print(result)