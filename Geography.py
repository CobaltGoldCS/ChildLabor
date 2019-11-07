
import requests
from bs4 import BeautifulSoup
import urllib.request
import time
#Needs authentication header with api- not in URL
apiKey = "8914d5ba-b5be-485d-90bc-7b0ec8ac2709"
url = "https://data.dol.gov/get/childlabor_sta/"
header = {"Accept": "application/json", "X-API-KEY": apiKey}
status = requests.get(url, headers=header)
print(status)
