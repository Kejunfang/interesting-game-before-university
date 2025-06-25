import random

def random_number_game():
    target_number=random.choice(range(1,101))
    attempts =0
    
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("欢迎游玩简单的数字猜数字游戏")
 
    while True:
        print("")
        guess=int(input("请输入1-100之间的整数:"))
        attempts += 1
        
        if guess == target_number:
            print("恭喜你猜对了！！！！")
            print(f"你作答了{attempts}次")
            break
        
        elif guess<target_number:
            print("太小了，再来一次")
        
        else:
            print("太大了，再来一次")
            
print(random_number_game())