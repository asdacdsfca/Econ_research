import requests
from bs4 import BeautifulSoup

session_requests = requests.session()

headers = {
'Host': 'www.utahcounty.gov',
'Connection': 'keep-alive',
'Cache-Control': 'max-age=0',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'Referer': 'https://www.utahcounty.gov/landrecords/SerialVersions.asp?av_serial=01:002:0001',
'Accept-Language': 'en-US,en;q=0.9',
'Cookie': 'ga_BFHRV55KT4=GS1.1.1689304461.1.1.1689305467.0.0.0; ASPSESSIONIDCEDBTACA=LPLDACDAFOGPOKAPIKPFDPGD; _gid=GA1.2.1182582373.1689641431; _ga=GA1.1.966284243.1689302850; _ga_03RXT0WNT6=GS1.1.1689706019.6.0.1689706019.0.0.0; _ga_LZQBPP7NCD=GS1.1.1689706019.6.0.1689706019.0.0.0; ASPSESSIONIDQGDBAAQQ=DNDFGDDDKPPLHMAGIDMMCOHH'
}

response = session_requests.get('https://www.utahcounty.gov/landrecords/property.asp?av_serial=10020001010', headers=mydict)
soup = BeautifulSoup(response.content, "html.parser")
soup

def scraper():
    url = "https://www.utahcounty.gov/landrecords/SerialVersions.asp?av_serial=01:002:0001"
    response = requests.get(url)

def find_names(soup):
    string_soup = str(soup)
    names_list = string_soup.split("av_name=")[1:]
    for i in names_list:
        splited_1 = i.split(">")
        splited_2 = splited_1[1].split("<")
        name = splited_2[0]
        print(name)