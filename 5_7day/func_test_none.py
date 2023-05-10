def add(a,b):
    """
    函数说明：两个数字相加
    :param a:
    :param b:
    :return:
    """
    re=a+b
    return re
add(1,2)

def f1():
    print("f1")
def f2():
    print("f2")
def f3():
    f1()
    f2()
    print("f3")
f2()
f3()