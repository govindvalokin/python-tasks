odd=[]
even=[]
oddsum=0
evensum=0
for i in range(15,36):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in odd:
    oddsum=oddsum+i
for i in even:
    evensum=evensum+i
print("oddsum= ",oddsum)
print("evensum= ",evensum)
    

