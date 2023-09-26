marks=[]
sum=0
for i in range(6):
    sub=int(input("enter your subject marks(0-100):"))
    marks.append(sub)
total=600
for i in marks:
    sum=sum+i
percentage=(sum/600)*100
print(percentage)
if percentage >= 90:
    print("GRADE = A+")
elif percentage < 90 and percentage >=80:
    print("GRADE = A")
elif percentage < 80 and percentage >=70:
    print("GRADE = B+")
elif percentage < 70 and percentage >=60:
    print("GRADE = B")
elif percentage < 60 and percentage >=50:
    print("GRADE = C")
elif percentage < 50 and percentage >=40:
    print("GRADE = D")
elif percentage < 40:
    print("GRADE = FAILED")
