import urllib.request

sample_url = "http://httpbin.org/xml"

resp = urllib.request.urlopen(sample_url)
print(resp.status)
print(resp.getheaders())
print(resp.getheader('Content-Type'))
print(resp.headers['Content-Type'])


#read data from web
data = resp.read().decode('utf-8')
print(data)

