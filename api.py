from flask import *
import random
import json 


app = Flask(__name__)

#@app.route('/Users/matsuuratsubasa/prog',methods = ['GET'])
@app.route('/',methods = ['GET'])
def get_str():
  # generate random number
  ran = random.random() * 10
  val = int(ran%3)
  print("ran is {} dev 3 is {} integrate val is {}".format(ran,ran%3,val))

  stri = "nan"
  if (val == 0):
    stri = "a" 
    return jsonify({'msg': stri}) 
  elif (val == 1):
    stri = "b"
  else:
    stri = "c" 
  return jsonify({}) 


#--------------------test ---------
@app.route('/')
def hello():
  name = "Hello World"
  return name


if __name__ == "__main__":
  app.run(port=8888)
