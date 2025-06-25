def add_task(todo_list,task):
    todo_list.append(task)
    print("Task has successfully added!")
    
def remove_task(todo_list,task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task has successfully removed!")
    else:
        print("The task is not in the list!")

def view_list(todo_list,task):
    print("Task list:")
    for idx,task in enumerate(todo_list,start=1):
        print(f"{idx},{task}")

def main():
    todo_list=[]
    while True:
        print("Welcome to use simple todo list!")
        print("1.Add task")
        print("2.Remove task")
        print("3.View Task")
        print("4.The end")
        
        choice=input("Please select your choice:")
        
        if choice == "1":
            task=input("please type your task:")
            add_task(todo_list,task)
        elif choice == "2":
            task=input("please the task you want to remove:")
            remove_task(todo_list,task)
        elif choice == "3":
            view_list(todo_list,task)
        elif choice =="4":
            print("Thank you!!!!!!!!")
            break
        else:
            print("Invalid value,Please try again!")
            
            
if __name__=="__main__":
    main()

    