import matplotlib.pyplot as plt

# chainging the color of the line

x = [10,20,30]
y = [5,7,3]

x2 = [25,40,60]
y2 = [26,24,26]

plt.bar(x,y,label = 'First Line',color = 'y')
plt.bar(x2,y2,label = 'Second Line',color = 'green')
plt.xlabel('Plot Number')
plt.ylabel('Importan Graph\nNew line')
plt.legend()
plt.show()