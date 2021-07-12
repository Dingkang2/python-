import numpy as np #sin arange 函数包
import matplotlib.pyplot as plt #plot 函数包

x = list(np.arange(-2*np.pi , 2*np.pi , 0.1))
y = np.sin(x)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = sinx')
plt.show()
