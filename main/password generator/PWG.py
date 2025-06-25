import random
import string

def random_password(length=12):
    characters=string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(characters)for i in range(length))
    return password

def main():
    choice = input("Welcome to simple password generator,to get start, please press 1:")
    if choice == "1":
        print("Password:",random_password())
    else:
        print("Invalid value,please try again!")

if __name__=="__main__":
    main()
