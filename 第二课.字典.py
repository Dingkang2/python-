#字典{}
dic1 = {'color':'red', 'score':'5'}
print(dic1['color']) #red
print(dic1['score']) #5

#添加元素
dic1['age'] = 18
print(dic1) #{'color':'red', 'score':'5', 'age':18}

#修改
dic1['age'] = 15

#删除
del dic1['age']

# keys values
dic1.keys() # 获取color score
dic1.values() # 获取 red 5
dic1.items() # 同时获取key value
dic1.get('score') # 5

#len 查看长度
len(dic1)

#复制字典
dic2 = dic1.copy() #id不同

#清空字典
dic1.clear()

dic3 = dic1
dic2 = dic1.copy()
dic1.clear() #dic1 = {}  dic2 = {'color':'red', 'score':'5'}
#             dic3 = {}