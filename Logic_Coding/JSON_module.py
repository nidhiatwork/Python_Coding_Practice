import urllib.request
import json

req = urllib.request.urlopen("http://httpbin.org/json")
data = req.read()
data = data.decode("utf-8")
print(data)

obj = json.loads(data)
print(obj["slideshow"]["author"])

for slide in obj["slideshow"]["slides"]:
    print(slide["title"])

data = {
  "slideshow": {
    "author": "Yours Truly", 
    "date": "date of publication", 
    "slides": [
      {
        "title": "Wake up to WonderWidgets!", 
        "type": "all"
      }, 
      {
        "items": [
          "Why <em>WonderWidgets</em> are great", 
          "Who <em>buys</em> WonderWidgets"
        ], 
        "title": "Overview", 
        "type": "all"
      }
    ], 
    "title": "Sample Slide Show"
  }
}
with open("json_output.json","w") as fp:
    json.dump(data, fp, indent=4)