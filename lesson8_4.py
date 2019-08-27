import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('lesson8_4.csv','r') as csvfile:
    plot = csv.reader(csvfile,delimiter = ',')

    for i in plot:
        x.append(int(i[0]))
        y.append(int(i[1]))

plt.plot(x,y,label = 'Loaded from the file', color = 'r')
plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.title('Lesson8_4.py')
plt.legend()

plt.show()