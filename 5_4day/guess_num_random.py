#随机数  random
import random
number=random.randint(1,10)
print(number)

guess_num=int(input("第一次：输入你猜测的数字:"))
if guess_num==number:
    print("猜对了！！")
else:
    if guess_num<number:
        print("猜小了，请重新输入：")
    else:
        print("猜大了，请重新输入：")

    guess_num = int(input("第二次：再次输入你猜测的数字:"))
    if guess_num == number:
        print("猜对了！！")
    else:
        if guess_num < number:
            print("猜小了，请重新输入：")
        else:
            print("猜大了，请重新输入：")
        guess_num = int(input("第三次：再次输入你猜测的数字:"))
        if guess_num == number:
            print("猜对了！！")
        else:
            print("三次都没有猜对！！")
            print(f"你要猜的数字是{number}")
