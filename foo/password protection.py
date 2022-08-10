# Kamran@123 = "67c36189f08cdf6487f0d5df5e7066c3"
""" Python Password Check """
import hashlib

password = "67c36189f08cdf6487f0d5df5e7066c3"


def main():
    # Code goes here
    print("Doing some stuff")
    exit(0)


while True:
    user_password = input("Enter password: ")
    if hashlib.md5(user_password.encode()).hexdigest() == password:
        print("welcome to the program")
        main()
    else:
        print("Wrong Password, try again")
