import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/"

r = requests.get(url)
print(r.text)
