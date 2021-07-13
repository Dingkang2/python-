#元组，无法进行修改的列表
tuple1 = (1, 2, 3, 4, 5)

#访问
tuple1[0]
tuple1[2:]

#切片
tuple2 = tuple1[1:]

#单个元素元组
tuple3 = (52,) #必须有逗号，否则为int
tuple4 = 52, #无括号也可

#拼接修改
xtuple = ("jack", "tom", "rose", "eric")
xtuple = (xtuple[0], "jarry") + xtuple[2:] #与前一个id不同
