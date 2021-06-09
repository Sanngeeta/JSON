# Q7.Text file data ko json file data mai convert karo,jaise ki neeche diya hai?

# Example:

# Input :-


# Text.txt:-  
#  Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29

import json

file ="Text.txt"

dict1={}

with open(file) as k:
    for i in k:
        key,dictonry=i.strip().split(None,1)
        dict1[key]=dictonry.strip()

new_file=open("newfile7.json","w")
json.dump(dict1,new_file)
new_file.close()

