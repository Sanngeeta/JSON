
# # Q.1 Json data ko python object main convert karne ka program likho?.

import json
with open("new.json","r") as k:

    data=json.load(k)
    print(data)









# # import json
# # a={"name":"dipak","age":21,"city":"pune"}
# # with open("s.json","w")as k:
# #     json.dump(a,k,indent=5)


















# list1=[1,2,3,4,5,6]
# dict1={}
# for i in list1:
#     if list1 not in dict1:
#         dict1.update(list1)
# print(dict1)