
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
apiKey = "9dee867e-35fc-41f3-ac05-f4b15c5aa310"
url = "https://data.dol.gov/get/childlabor_sta/?KEY="
fullUrl = url+apiKey
header = {"Accept": "application/json"}
status = requests.get(url, headers=header)
print(status.json())
