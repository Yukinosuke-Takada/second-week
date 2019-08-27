import matplotlib.pyplot as plt


pop_ages = [12,20,23,34,45,56,63,67,73,78,79,90,95,100,150]

idx = [ x for x in range(len(pop_ages))]

plt.bar(idx, pop_ages, label = 'Ages of people')

plt.xlabel('x')
plt.ylabel('y')

plt.legend()
plt.show()
