import matplotlib.pyplot as plt


pop_ages = [12,20,23,34,45,56,63,67,73,78,79,90,95,100,150]

bins = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(pop_ages,bins,histtype = 'bar',rwidth = 0.7)
plt.legend()

plt.show()