#end''为不换行
# print("hello ",end='')
# print("world ",end='')
print("九九乘法表如下：")
i=1
while i<=9:
    j=1

    while j<=i:
        print(f"{i}*{j}={i*j}\t",end='')
        j+=1
    i+=1
    print()
print("以上是乘法表！！！")
