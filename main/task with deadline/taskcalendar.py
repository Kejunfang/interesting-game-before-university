import calendar

def add_task(task_list,task):
    task_list.append(task)
    print("Your task has added!!!")

def remove_task(task_list,task):
    if task in task_list:
        task_list.remove(task)
        print("Task has removed!!!")
    else:
        print("Task is not in Tasklist!!!")

def view_task(task_list):
    print("Task list:")
    for idx,(task,deadline) in enumerate(task_list,start=1):
        print(f"{idx}.{task}(deadline:{deadline})")

def main():
    task_list=[]
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`")
        print("Welcome to use simple todo-list!")
        print("1.Add task")
        print("2.Remove task")
        print("3.View task")
        print("4.Goodbye")
        
        choice=input("Please select your chioce:")
        if choice == "1":
            task=input("Please add your task:")
            deadline=input("Please enter the deadline(YYYY-MM-DD):")
            add_task(task_list,(task,deadline))
        elif choice == "2":
            task=input("Please enter the task you want to remove:")
            deadline=input("Please enter the deadline:")
            remove_task(task_list,(task,deadline))
        elif choice == "3":
            view_task(task_list)
        elif choice == "4":
            print("Thank you!!!See you again!")
            break
        else:
            print("Inalid value,please enter again!")
            
if __name__=="__main__":
    main()