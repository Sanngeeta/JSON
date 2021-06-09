import json

num={"name": "David",
     "class":"I",
     "age": 6  
 }

with open("my_file2.json","w") as k:
    json.dump(num,k,indent=4)





