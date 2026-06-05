
import socket , requests
#from bs4 import BeautifulSoup

url = "http://httpbin.org/get"

headers = {'User-Agent': ''}
response = requests.get(url,headers=headers)
print(response.status_code)