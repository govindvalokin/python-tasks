id=int(input("enter your ID:"))
name=input("enter your name:")
basic_pay=int(input("enter the basic pay:"))
if basic_pay>10000:
    hra=(basic_pay*15)/100
    da=(basic_pay*8)/100
    netpay = basic_pay+hra+da
    print("HRA=",hra)
    print("DA=",da)
    print("NETPAY=",netpay)
if basic_pay<10000 and basic_pay>5000:
    hra=(basic_pay*10)/100
    da=(basic_pay*5)/100
    netpay = basic_pay+hra+da
    print("HRA=",hra)
    print("DA=",da)
    print("NETPAY=",netpay)
if basic_pay<5000:
    hra=(basic_pay*5)/100
    da=(basic_pay*3)/100
    netpay = basic_pay+hra+da
    print("HRA=",hra)
    print("DA=",da)
    print("NETPAY=",netpay)