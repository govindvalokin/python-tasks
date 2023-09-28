list1=[]
list2=[]
dict={}
for i in range(5):
    sample1=int(input("enter your num for list1:"))
    list1.append(sample1)
c1 = len(list1)
for i in range(4):
    sample2=int(input("enter your num for list 2:"))
    list2.append(sample2)
c2 = len(list2)
if c1<c2:
    for i in range(c1):
        dict[list1[i]]=list2[i]
elif c2<c1:
    for i in range(c2):
        dict[list1[i]]=list2[i]
print(dict)