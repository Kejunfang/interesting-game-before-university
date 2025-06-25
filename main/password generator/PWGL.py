import random
import string

def random_password(length=12,):
    characters=string.ascii_letters + string.digits + string.punctuation
    password= ''.join(random.choice(characters)for i in range(length))
    return password
    
def add_password(task_list,password):
    task_list.append(password)

def view_pass(task_list,password):
    print("Password list:")
    for idx,(password,use) in enumerate(task_list,start=1):
        print (f"{idx}.{password} (use:{use})")

def main():
    task_list=[]
    while True:
        print("Welcome to use simple password generator!")
        print("1.Generate password")
        print("2.View password")
        print("3.Goodbye")
    
        choice=input("Please select your choice:")
        if choice == "1":
            use=input("For what:")
            password=random_password(length=12)
            print("Password:",password)
            add_password(task_list,(password,use))        
        elif choice == "2":
            view_pass(task_list,password)
        elif choice == "3":
            print("Thank for using!Goodbye!")
            break
        else:
            print("Invalid value,Please try again!")
        
if __name__ == "__main__":
    main()