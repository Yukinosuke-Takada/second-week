import matplotlib.pyplot as plt

'''
days = [1,2,3,4,5]
sleeping = [7,8,9,10,7]
eating = [2,4,5,6,8]
working = [2,3,6,7,8]
playing = [8,7,9,1,3]
'''

slices = [2,4,5,6]

act = ['sleeping','eating','working','playing']
cols = ['green','blue','red','yellow']

plt.pie(slices, labels = act, colors = cols, startangle = 90 ,)

#plt.xlabel('X-label')
#plt.ylabel('Y-label')
plt.title('Lesson8_1.py')
plt.legend()

plt.show()

