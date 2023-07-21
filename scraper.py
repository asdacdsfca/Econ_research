import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


headers_dict = {
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

names = dict()

def requests_attempt(url):
    session_requests = requests.session()
    response = session_requests.get(url, headers=headers_dict)
    soup = BeautifulSoup(response.content, "html.parser")
    name_ind = set(find_names(soup))
    names.update({"": name_ind})
    
    

data_fp = os.path.join('data', 'address_point.csv')
address = pd.read_csv(data_fp)

def scrape_verify():
    numb_lst = [str(i) for i in range(99)]
    tries = [str(i) if len(str(i)) >= 2 else '0' + str(i) for i in numb_lst]
    for change in tries:
        url = f"https://www.utahcounty.gov/landrecords/property.asp?av_serial=4149900{change}004"
        requests_attempt(url)
        try:
            print(requests_attempt(url))
        except:
            continue

def scraper():
    url = "https://www.utahcounty.gov/landrecords/SerialVersions.asp?av_serial=01:002:0001"
    response = requests.get(url)

def find_names(soup):
    names_store = []
    string_soup = str(soup)
    names_list = string_soup.split("av_name=")[1:]
    for i in names_list:
        splited_1 = i.split(">")
        splited_2 = splited_1[1].split("<")
        name = splited_2[0]
        names_store.append(name)
    return names_store