print("5/2=",5/2)     #这是一个浮点数
print("5//2",5//2)    #这是一个保留整数的
print("2**2",2**2)    #**是次方

name ="123"
age=18
number=100
print("my name is "+name+" age is 18") #+号只能拼接字符串类型
print("my age is %s my number is %s" % (age,number))  #字符串拼接使用%来占位
print(f"my name is:{name} ,my age is:{age}")  #字符串拼接使用{}来表示，不理会类型，不会精度控制
