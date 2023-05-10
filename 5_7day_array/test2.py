myllist=['abc',"itcast","bbb"]
index=myllist.index("abc")
print(index)
myllist[0]="aaa"
print(myllist)
myllist.insert(0,"no1")
print(myllist)
myllist.append("最后")  #最后追加一个
print(myllist)
myllist.extend(["追加一批","111"]) #最后追加一批
print(myllist)
myllist=['abc',"itcast","bbb"]
del myllist[2]  #del 删除指定元素
print(myllist)
myllist=['abc',"itcast","bbb"]
myllist.pop(2)  #pop 删除元素，pop可以将元素取出
print(myllist)
myllist=['abc',"itcast",'abc',"itcast","bbb"]
myllist.remove("abc")  #remove为删除第一个出现要删除的元素，
print(myllist)
myllist.clear()  #clear 清空
print(myllist)
myllist=['abc',"itcast","bbb",'abc']
count=myllist.count("abc")  #count统计某一元素出现的次数
print(count)
length= len(myllist) #len 输出列表中有多少元素
print(length)