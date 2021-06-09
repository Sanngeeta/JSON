# Q4.Python dictionary(sort by key) object ko json data ::mai convert karne ka program likho? Example: Input :- Output:- JSON data:

# import json
# k={
#     '4': 5, 
#     '6': 7, 
#     '1': 3, 
#     '2': 4}
# with open("my_file4.json","w") as y:
#     json.dump(k,y,indent=4,sort_keys=True)
   
    

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dict1={}
for i in range(len(keys)):
    for x in range(len(values)):
        dict1.update({keys[i]:values[x]})
print(dict1)


# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict4={}
# for i in dict1,dict2:
#     dict4.update(i)
# print(dict4)
   

# Exercise 5: Create a new dictionary by extracting the following keys from a below dictionary
# {'name': 'Kelly', 'salary': 8000}
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]
dict1={}
for i in keys:
    dict1.update({i:sampleDict[i]})

print(dict1)



# newDict = {k: sampleDict[k] for k in keys}
# print(newDict)