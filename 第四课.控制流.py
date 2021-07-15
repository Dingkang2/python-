# if
'''
name = str(input('你的名字'))
if name == 'jack':
    print('hello jack')
elif name == 'eric':
    print('hello eric')
elif name == 'koko':
    print('hello koko')
else:
    print('hello ' + name)
'''
'''
score = int(input('请输入你的成绩'))
if score < 60 :
    print('不及格')
elif score >= 60 and score < 75 :
    print('及格')
elif score >= 75 and score < 90 :
    print('良好')
else:
    print('优秀')
'''
# while
'''
while True:
    name = str(input('请输入名字'))
    if name == 'jack':
        break
print('thank you')
'''
# continue 使程序循环回到开始处
'''
while True:
    name = str(input('请输入名字'))
    if name != 'jack':
        continue
    elif name == 'jack':
        break
    print('hello jack') 
print('thank you')
'''
# for 
'''
for i in range(5):
    print('hello python' + '(' + str(i) +')')
'''
'''
total = 0
for i in range(101):
    total = total + i
print(total)

for i in range(10, 15):
    print(i)

for i in range(0, 10, 2):
    print(i)
for i in range(20, 0, -2):
    print(i)
'''
# sys.exit()
import sys
while True:
    print('type exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('xxxx')
