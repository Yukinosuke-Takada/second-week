import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

rn = np.random.rand(10)

print(rn)

style.use('ggplot')

plt.plot(rn, 'g',label = 'first one', linewidth = 2)

plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.title('Lesson9_1.py')
plt.legend()

plt.show()