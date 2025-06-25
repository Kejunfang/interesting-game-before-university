def add_information(inf_list,information):
    inf_list.append(information)
    print("信息添加成功！")
    
def view_information(inf_list):
    print("个人信息：")
    for idx,(name,age,ic) in enumerate(inf_list,start=1):
        print(f"{idx}.Name:{name}")
        print(f"2.Age:{age}")
        print(f"3.IC No:{ic}")
    
def main():
    inf_list= []
    while True:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("欢迎使用简易的个人管理系统")
        print("1.添加个人信息")
        print("2.查看个人系统")
        print("3.退出程序")
        
        choice=input("请做出选择：")
        
        if choice == "1":
            inf_list=[]
            name=input("请输入你的名字：")
            age =input("请输入你的年龄：")
            ic = input("请输入你的身份证：")
            add_information(inf_list,(name,age,ic))
            
        elif choice == "2":
            view_information(inf_list)
        
        elif choice == "3":
            print("感谢使用！！！")
            break
        else:
            print("输入错误，请重新输入")
            
if __name__ == "__main__":
    main()