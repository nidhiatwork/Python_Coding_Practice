import requests
payload = {'user_name': 'admin', 'password': 'password'} 
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url) 
print(r.text)

# Handling timeouts:
requests.get('http://www.google.com', timeout=1)  

# Handling cookies:
# import requests 
r = requests.get('http://www.examplesite.com') 
r.cookies['cookie_name'] 


custom_cookie = {'cookie_name': 'cookie_value'} 
r = requests.get('http://www.examplesite.com/cookies', cookies=custom_cookie) 


url = 'http://ip.jsontest.com/'
Data = {'nidhi':"123", 'bhushan':"456"}
response = requests.post(url, data=Data, headers={"Content-Type": "application/json"})
print(response.text)


# Send files
url = 'http://httpbin.org/post' 
file_list = [ ('image', ('image1.jpg', open('image1.jpg', 'rb'), 'image/png')), ('image', ('image2.jpg', open('image2.jpg', 'rb'), 'image/png')) ] 
r = requests.post(url, files=file_list) 
print(r.text) 


# Others

requests.put('url', data={'key': 'value'}) 
requests.delete('url') 
requests.head('url') 
requests.options('url') 

# For downloading contents from API and save on local:
import requests
payload = {'user_name': 'admin', 'password': 'password'} 
r = requests.get('http://httpbin.org/get', params=payload)
c = open("text.txt", 'wb')
for chunk in r.iter_content(chunk_size=25):
    if chunk:
        c.write(chunk)