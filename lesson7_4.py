import matplotlib.pyplot as plt

# histogram (distrbution)

# this is a bar chart
x = [11,30,60,100,150]
y = [30,40,50,60,70]

x2 = [0,5,10]
y2 = [50,60,70]

plt.bar(x,y, label = 'First')
plt.bar(x2,y2, label = 'Second')

plt.legend()
plt.show()

