import matplotlib.pyplot as plt

# legends

x = [1,2,3]
y = [5,7,3]

x2 = [2,4,6]
y2 = [26,24,26]

plt.plot(x,y,label = 'First Line')
plt.plot(x2,y2,label = 'Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Importan Graph\nNew line')
plt.legend()
plt.show()

