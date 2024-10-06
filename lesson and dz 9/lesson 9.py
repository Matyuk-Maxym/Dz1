import urllib.request
import requests
opener = urllib.request.build_opener()

# response = opener.open('https://httpbin.org/get')
#
# print(response.read())
#
# response = requests.get('https://httpbin.org/get')
# print(response.content)
# print(response.text)


response = requests.post('https://httpbin.org/post', data="Hello B2114" , headers={'Content-Type': 'text/html'})
print(response.text)