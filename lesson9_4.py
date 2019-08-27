import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

axes = fig.add_axes([0.15,0.12,0.8,0.8])

x = np.linspace(-10,10,200)
y = np.cos(x)

axes.plot(x,y,'b--')

plt.title('y = cos(x)')


plt.xlabel('X')
plt.ylabel('Y')

# plt.show()

fig.savefig('graph.pdf')


# ax.legend(loc=1) # upper right corner
# ax.legend(loc=2) # upper left corner
# ax.legend(loc=3) # lower left corner
# ax.legend(loc=4) # lower right corner

