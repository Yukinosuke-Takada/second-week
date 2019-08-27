import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,5,40)
y = x**2
print(x)
print(y)

plt.plot(x,y,'r')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.title('Lesson9_1.py')
# plt.show()

plt.subplot(1,2,1)
plt.plot(x,y,'r--')
plt.subplot(1,2,2)
plt.plot(y,x,'g*-')
plt.show()