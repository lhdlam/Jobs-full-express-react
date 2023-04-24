import requests
import json
import random

url = "https://elbdev01.bucs.belx.co.jp:8000/api/v1/get_teiban_hacchu_nyuryoku/"

with open("jancd.txt", "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]


while(True):
  random_number = random.randint(0, 200)
  payload = json.dumps({
    "ten_cd": "0001315",
    "jan_cd": lines[random_number],
    "haitatsu_date": "20221222"
  })
  headers = {
    'x-token': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0YW50b19jZCI6IjM3NTYiLCJwYXNzd29yZCI6IjM3NTYiLCJpc19hY2Nlc3MiOjEsImV4cCI6MTY4MjA0NzMwMH0.5COQ7jXzOO1kah6xGmP4F7GGVZMxcTuR5KgAifkUTvI',
    'device-id': '123456',
    'Content-Type': 'application/json',
  }

  response = requests.request("POST", url, headers=headers, data=payload)

  print(response.text)