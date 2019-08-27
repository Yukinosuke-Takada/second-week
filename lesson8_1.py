import matplotlib.pyplot as plt

x = [1,2,3,4,5,6,7,8,9]
y = [2,9,3,8,3,6,9,6,2]

# for scatter graph

plt.scatter(x,y, label = 'scatter plot', color = 'green',marker = '*',s = 100)

plt.xlabel('X-label')
plt.ylabel('Y-label')
plt.title('Lesson8_1.py')
plt.legend()
plt.show()
