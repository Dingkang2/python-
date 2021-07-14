'''
def firstfunction(name):
    print('I love ' + name)

firstfunction('ding')
for num in range(3):
    firstfunction('ding')
'''
'''
def addfunction(num1, num2):
    print(num1 + num2)
addfunction(2, 3)
'''
#return 返回值
'''
def div(num1, num2):
    if num2 == 0:
        return '除数不能为零'
    else:
        return num1 / num2
div(9, 3)
'''
#实际参数 形式参数，实参 形参
"""
def exchangerate(dollar):
    '''
    功能 汇率换算
    汇率 XXX
    日期 XXX
    '''
    #return dollor * 6
    print(dollar * 6)
exchangerate(100)
print(exchangerate.__doc__)
"""
def myfunction(name, score):
    print(name + '分数是' + str(score))

myfunction('jack', 66)
myfunction(score = 66, name = 'jack') #关键字参数

def saylove(name = 'python'): #默认参数‘python’
    print('I love ' + name)
saylove('ding') #参数可修改

def anfunction(name = 'python', perform = True):
    sentence = name + '表现'
    if perform:
        sentence = sentence + '很好'
    else:
        sentence = sentence + '一般'
    print(sentence)
anfunction(name = 'matlab', perform = False)

def testfunction(*params): #参数数目不确定，收集参数
    print("有 %d 个函数" % len(params))
testfunction(1, 2, 3, 4)