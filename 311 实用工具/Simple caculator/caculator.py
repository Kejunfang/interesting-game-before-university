def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y ==0 :
        return("Wrong!!!You are dividing zero!")
    else:
        return x /y

print("Welcome to use simple caculator!")

print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Please make a choice:")
if choice in ("1","2","3","4"):
    num1=float(input("Please enter your first number:"))
    num2=float(input("Please enter your second number:"))
    
    if choice == "1":
        print("Your answer is:",add(num1,num2))
    elif choice == "2":
        print("Your answer is:",subtract(num1,num2))
    elif choice == "3":
        print("Your answer is:",multiply(num1,num2))
    elif choice == "4":
        print("Your answer is:",divide(num1,num2))
    
else:
    print("Invalid number!!!!")