import matplotlib.pyplot as plt
import csv
import numpy as np


x,y = np.loadtxt('lesson8_4.csv', delimiter= ',',unpack = True)

plt.plot(x,y,label = "Easy way to use")
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.title('Lesson8_5.py')
plt.legend()

plt.show()