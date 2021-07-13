#列表 list
number = [1, 2, 3, 4]

#添加元素
number.append(6) #只能在末尾添加一个

number.extend([7, 8]) #添加多个元素末尾

number.insert(0, 0) # insert（a,b）在 a 位置添加 b 元素，从零开始
number.insert(-1,11) # 添加在后部一位置，从0开始

#获取元素
number[4] # number第四个值，从-1开始

#删除元素
number.remove(8) #删除元素 8

number.pop(4) #删除位置为8的元素，从零开始。不给索引值，默认最后一个元素

del number(0) #删除位值0的元素

#切片
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
number2 = number[0:4] #0 开始位置，4结束位置，结束位置不包含进来
number3 = number[:4]
number4 = number[4:]
number5 = number[0:6:2] #2 访问步长
number6 = number[::-1] #列表反转

#拼接
list1 = [12, 13]
list2 = [14, 15]

list3 = list1 + list2
list4 = list1*3 #[12, 13, 12, 13, 12, 13]

#判断是否在列表中
3 in number #True

#列表元素种类
list5 = [1, 2, "hello", ["jack", "rose"]]

#列表计数、寻址、反转、排序
number.count(2) #计算元素出现的次数
number.index(1) #元素出现的位置
number.reverse() #列表反转
number.sort() #列表排序

dir(list) #列出列表功能函数