'''
import random

num = random.randint(1,10)
tcmp = input('猜猜我想的数字是几？') #用户输入
guess = int(tcmp)
times = 1
while(guess != num) and (times < 3):
    if guess < num:
        print("猜小了")
    else:
        print("猜大了")
    tcmp = input('猜猜我想的数字是几？')
    guess = int(tcmp) #用户输入赋值guess
    times = times + 1
if (guess != num) and (times >= 3):
    print("猜太多次了")
else:
    print("猜对了")
'''
'''
score = int(input("输入成绩:"))

if 100 >= score >= 90:
    print('A')
elif 90 > score >= 80:
    print('B')
elif 80 > score >= 70:
    print('C')
elif 70 > score >= 60:
    print('D')
else:
    print('不及格')
'''
'''
sum = 0
for i in list(range(1,101,1)):
    sum = sum + i
print(sum)
'''

