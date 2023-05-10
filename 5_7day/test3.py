num=10
def f1():
    num=20
    print(num)
# f1()

def f2():
    global num  #global函数内部定义的变量为全局变量
    num=30
    print(num)
f2()
print(num)

