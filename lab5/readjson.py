import json
import re
file=open("tweet.json","r")
accounts=json.load(file)
pattern=r'[a-zA-Z]+'
id_list=[]
for i in accounts:
    if re.fullmatch(pattern, i["user.screen_name"]):
        id_list.append(i["id"])
id_list.sort()
wfile=open("ans.txt","w")
for i in id_list:
    print(i)
file.close()