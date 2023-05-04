import  random
num=random.randint(1,100)
count=1
guess=int(input("请输入你猜测的数字:"))

while guess!=num:
    if guess<num:
        print("猜xiao了，")
        guess=int(input("重新输入:"))
        count+=1
    else:
        print("猜da了，")
        guess = int(input("请重新输入:"))
        count+=1
print(f"猜对了，数字就是{num}")
print(f"你一共采了{count}次")