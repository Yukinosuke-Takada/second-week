import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,5,100)

y = x**2
print('x: ', x)
print('y: ', y)

# function 

print(plt.plot(x,y))

plt.show()


    