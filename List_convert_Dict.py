list1=["sangeeta","1","pooja","2","khushboo","3","neha","4"]
dic={}
for i in range(0,len(list1),2):
        dic.update({list1[i]:list1[i+1]})
  
print(dic)
