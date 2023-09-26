name1 = input("enter your name:")
name2 = input("retype the name:")
password1 = input("enter the password:")
password2 = input("retype password:")
if name1==name2:
    print("name matching")
else:
    print("name mismatch")
if password1==password2:
    print("password matching")
else:
    print("password mismatch")