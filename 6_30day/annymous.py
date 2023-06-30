#匿名函数，函数调用函数
def test(compute):
    result=compute(1,2)
    print(result)

def compute(x,y):
    return x+y

test(compute)

#lambda 关键字的使用
def test(compute):
    result=compute(1,2)
    print(result)
test(lambda x,y: x+y)