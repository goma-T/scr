import requests 
import json 


# api get information about price
def get_message():
  resoponse = requests.get('http://127.0.0.1:8888/')
  #print(resoponse.json())
  return json.dumps(resoponse.json())

# decorde value
def decorde_val(stri):
  del_yen = stri.replace("円"," " )
  del_dot = del_yen.replace(",","" )
  val = float(del_dot) 
  if val > 1000 :
    print(val) 

# judge value
def judge_value(stri):
  #tmp = stri.object.get["msg"]
  tmp = json.loads(stri)
  val_str = tmp.get("msg")
  #print (val_str)
  decorde_val(val_str)
  

# send line 
def send_message(stri):
  url = "https://notify-api.line.me/api/notify"
  access_token = 'hhaXTtDEaiQI3IWYPZAXZxTHHaXTyBrYL8CDurYD3qM'
  headers = {'Authorization': 'Bearer ' + access_token}
  payload = {'message' : stri}
  r = requests.post(url, headers=headers , params = payload)

if __name__ == "__main__":
  stri = get_message()
  if stri=="{}": 
    print("null")
  else:
    judge_value(stri)
    send_message(stri)
  






