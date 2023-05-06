i=1
j=1
print("九九乘法表如下：")
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{i}*{j}={i*j}\t",end='')
    print()
print("以上便是九九乘法表！！！")