import requests
import json
import random

url = "https://elbdev01.bucs.belx.co.jp:8000/api/login/"


while(True):
  random_number = random.randint(10000,99999)
  payload = json.dumps({
    "tanto_cd": str(random_number),
    "password": str(random_number),
  })
  headers = {
    'Content-Type': 'application/json'
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)