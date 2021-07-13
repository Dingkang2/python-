#集合
num = {1, 2, 3, 3, 4, 5, 6, 6, 7}
#>> num   输出{1，2，3，4，5，6，7}，自动删除重复数字
# X num[1] 不可用索引

#集合与列表
set1 = set(['jack', 'rose', 'eric'])

#添加元素
set1.add('jarry')

#删除元素
set1.remove('jarry')

#冻结
set1 = frozenset({'jarry', 'rose', 'eric'})