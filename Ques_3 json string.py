
# Q.3 Python object ko json string mai convert karne ka program likho?

import json
dict1='{"name":"Rahul","age":20,"city":"Delhi","study":"BA progaramm"} '
k=json.dumps(dict1,indent=6)
print(k)



