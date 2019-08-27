import matplotlib.pyplot as plt
import numpy as np

fig , axes = plt.subplots(nrows = 1, ncols = 3)

x = np.linspace(0,5,40)
y = x**2

for ax in axes:
    ax.plot(x,y,'b')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('thai')

plt.tight_layout()


plt.show()


