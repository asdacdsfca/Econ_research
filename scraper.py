import requests
from bs4 import BeautifulSoup

def scraper():
    url = "https://www.utahcounty.gov/landrecords/SerialVersions.asp?av_serial=01:002:0001"
    response = requests.get(url)