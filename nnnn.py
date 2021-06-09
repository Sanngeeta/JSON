import json

# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'

# # parse x:
# y = json.loads(x)
# print(y)
# print(type(y))



# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y) 
# print(type(y))


import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
# print(json.dumps(x, indent=1))
print(json.dumps(x, indent=4, separators=(". ", " = ")))


# # Json convert to python
# import json
# a='{"name":"joha","age":12,"city":"pune"}'
# b=json.loads(a)
# print(b)
# print(type(b))

# import json
# a='{"name":"joha","age":12,"city":"pune"}'
# j=json.dumps(a)
# print(j)
# print(type(j))
# python to convert json


import json
age=20
print(json.dumps(age))

