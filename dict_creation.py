list=[]
dict={}
count1=[]
for i in range(5):
    sample=input("enter the words: ")
    list.append(sample)
for i in range(5):
    count1.append(list.count(list[i]))
print(count1)
for i in range(5):
    dict[list[i]]=count1[i]
print(dict)
