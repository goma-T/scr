from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import datetime 

stock_number = 9434 
url = 'https://kabuoji3.com/stock/{}/'.format(stock_number)

headers = {
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Safari/605.1.15"
}
soup = BeautifulSoup(requests.get(url).content,'html.parser')

print soup


