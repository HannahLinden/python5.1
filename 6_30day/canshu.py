def print_info(name ,age, gender):
    print(f"姓名:{name}  年龄:{age}  性别:{gender}")

#位置参数
print_info("小明",18,"男")

#关键字参数（顺序可以定义不一样的顺序)
print_info(name="hananh",age=20,gender="nv")

#缺省参数
def print_info2(name ,age, gender="男"):
    print(f"姓名:{name}  年龄:{age}  性别:{gender}")
print_info2("lisa",20)
print_info2("rose",40,"nv")

#不定长参数
def info(*args):
    print(f"args的类型是{type(args)},内容是{args}")
info(1,2,4)

def info2(**kwargs):
    print(f"args的类型是{type(kwargs)},内容是{kwargs}")
info2(name="a",age=14,gender="nv")
