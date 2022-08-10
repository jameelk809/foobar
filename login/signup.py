def choices():
    print("Please choose what you would like to do.")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
        return getdetails()
    elif choice == 2:
        return checkdetails()
    else:
        raise TypeError


def getdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt", 'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("User_Data.txt", 'w')
    info = info + " " + name + " " + password
    f.write(info)


def checkdetails():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("User_Data.txt", 'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Please Sign Up."


print(choices())
