'''
def discount(price, rate):
    final_price = price * rate
    print(final_price)
old_price = float(input('输入原价'))
rate = float(input('输入折扣'))
new_price = discount(old_price, rate)
'''
count = 5
def myfun():
    count = 10
    print(count)
myfun()
print(count)

#global
count = 5
def myfun():
    global count
    print(count)
myfun()
print(count)

def fun1():
    print('调用函数1')
    def fun2():
        print('调用函数2')
    fun2()
fun1()

x = 10
def fun3():
    x = 20
    def fun4():
        x = 30
        print(x)
    fun4()
fun3()

#返回函数,闭包
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of
square = nth_power(2)
cube = nth_power(3)
print(square(2))
print(cube(2))

#lambda 关键字
def add(x,y):
    return x + y

g = lambda x, y : x + y
print(g(1,2))

def add2(x):
    return lambda y : x + y
temp = add2(5)
print(temp(4))