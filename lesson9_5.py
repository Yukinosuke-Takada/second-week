import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

axes1 = fig.add_axes([0.15,0.12,0.8,0.8])
axes2 = fig.add_axes([0.25,0.62,0.35,0.25])

x = np.linspace(0,5,40)
y = x**2

axes1.plot(x,y,'b')

axes2.plot(y,x,'g')

axes1.set_title('Nothing')
plt.show()