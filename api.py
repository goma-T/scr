# coding: UTF-8
from flask import *
import random
import json 
import requests
from bs4 import BeautifulSoup


app = Flask(__name__)

#@app.route('/Users/matsuuratsubasa/prog',methods = ['GET'])
@app.route('/',methods = ['GET'])
def get_str():
  stock_number = 9434
  url = 'https://www.nikkei.com/nkd/company/?scode={}'.format(stock_number)

  # URLにアクセスする htmlが帰ってくる → <html><head><title>経済、株価、ビジネス、政治のニ
  html = requests.get(url=url)

  # htmlをBeautifulSoupで扱う
  soup = BeautifulSoup(html.content,"html.parser")
  #span = soup.find_all("span")
  dd = soup.find_all("dd")

  nikkei_heikin = ""

  tmp = soup.find(class_="m-stockPriceElm_value")
  tmp = tmp.text
  print(tmp)
  return jsonify({'msg': tmp}) 



#--------------------test ---------
@app.route('/')
def hello():
  name = "Hello World"
  return name


if __name__ == "__main__":
  app.run(port=8888)
