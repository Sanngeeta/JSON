


# ab aapko 4 dictionaries create karni hai jaise ki emp1 emp2 emp3 and emp4. har ek employee ka dictionary main name,designation,age and salary honi chahiye. aur ye sab dictionary ki keys hai jismai maine list main value di hai. Iska use kar ke aapko ek json file create karni hai? Jaise ki niche diya hai.
# Q8.Tumhare pass four employes ki details hai list mai:-
import json
list1=["neelam","programer","24","2400",]
list2=["komal","trainer","24","20000"]
list3=["anuradha","HR","25","40000"]
list4=["Abhishek","manager","29","63000"]  
key=["name","designation","age","salary"]
emp1={} 
emp2={} 
emp3={}
emp4={}

dict1={"emp1":emp1,"emp2":emp2,"emp3":emp3,"emp4":emp4}

for a in range(len(list1)):
    emp1.update({key[a]:list1[a]})
    for b in range(len(list2)):
        emp2.update({key[b]:list2[b]})
        for c in range(len(list3)):
            emp3.update({key[c]:list3[c]})
            for d in range(len(list4)):
                emp4.update({key[d]:list4[d]})
with open("file8.json","w") as k:
    json.dump(dict1,k,indent=5)