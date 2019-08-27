import matplotlib.pyplot as plt

num1 = [1,2,3,4,5,6]
num2 = [4,6,1,6,1,5]
num3 = [2,6,8,3,6,3]
num4 = [3,4,5,6,7,8]
num5 = [9,1,9,1,9,1]

# if u want have a label

plt.plot([],[],label = 'sleeping',color = 'green')
plt.plot([],[],label = 'working',color = 'red')
plt.plot([],[],label = 'training',color = 'yellow')
plt.plot([],[],label = 'resting',color = 'blue')

plt.legend()

plt.stackplot(num1,num2,num3,num4,num5,colors = ['green','red','yellow','blue'])
plt.show()


