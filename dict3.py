list=[]
dict={"thomas":68,"tom":32,"jack":78}
for i in range(6):
    sample=int(input("enter the numbers:"))
    list.append(sample)
print(list)
list2=dict.values()
new=[]
print(list2)
for i in list:
    if i in list2:
        new.append(i)#doubt?what will happen in case of remove?
print(new)