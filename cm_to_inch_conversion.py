length = int(input("enter the length in cm:"))
if length <=0:
    print("entry is invalid")
else:
    newlength=(length/2.54)
    print("length in inches= ",newlength)