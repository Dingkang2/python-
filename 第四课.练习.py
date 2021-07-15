import sys

while True:
    age = input('请输入你的年龄')
    if age == 'exit':
        sys.exit()
    else:
        age = int(age)
    if age < 3 and age >0:
        print('免费')
    elif age <= 0:
        print('error')
    elif age >= 3 and age < 12:
        print('10元')
    else:
        print('15元')
    