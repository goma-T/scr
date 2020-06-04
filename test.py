import requests 
import json 


# api get information about price
def get_message():
  resoponse = requests.get('http://127.0.0.1:8888/')
  #print(resoponse.json())
  return json.dumps(resoponse.json())

# judge value
def judge_value(stri):
  payload = {'message' : stri}
  print (stri) 
  print (payload)
  

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
  






