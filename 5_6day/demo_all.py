sum=10000
import random
for i in range(1,20):
    x=random.randint(1,10)
    if x>=5:
        if sum>0:
            print(f"绩效为：{x}；给员工{i}发工资1000元！！")
            sum-=1000
        else:
            print("余额为0，下个月再发！！")
            break
    else:
        print(f"绩效为：{x};不给员工{i}发工资！！")
