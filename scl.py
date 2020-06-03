# coding: UTF-8
import requests
from bs4 import BeautifulSoup

# アクセスするURL
#url = "http://www.nikkei.com/"
#url = "https://www.nikkei.com/markets/kabu/"
stock_number = 9434
url = 'https://www.nikkei.com/nkd/company/?scode={}'.format(stock_number)

# URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニュース:日経電子版</title></head><body....
html = requests.get(url=url)

# htmlをBeautifulSoupで扱う
soup = BeautifulSoup(html.content,"html.parser")
#span = soup.find_all("span")
dd = soup.find_all("dd")

nikkei_heikin = ""

tmp = soup.find(class_="m-stockPriceElm_value")
tmp = tmp.text
print(tmp)
