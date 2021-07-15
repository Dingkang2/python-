import random
import sys

while True:
    num = random.randint(0, 2)
    gauss = input('猜猜我想的数字')
    if gauss == 'exit':
        sys.exit()
    else:
        gauss = int(gauss)
    if gauss == num:
        print('猜对了')
    else:
        print('猜错了')