import json
import requests

url = "https://www.reddit.com/r/CryptoMoonShots/.json"
json_post = requests.get(url, headers={"user-agent": "proje"}).json()
json_data = json_post["data"]
json_child = json_data["children"]

for post in json_child:
  post_data = post["data"]
  post_text = post_data["selftext"]
  cnt = 0
  for i in range(0, len(post_text)-5):
    if cnt:
      break
    if post_text[i]=='t' and post_text[i+1]=='.' and post_text[i+2]=='m':
      for j in range(i+3, len(post_text)-4):
        if post_text[j]==" " or post_text[j]==']' or post_text[j]==')':
          print(post_text[i:j-1])
          cnt = 1
          break
