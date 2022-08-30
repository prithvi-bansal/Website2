import matplotlib.pyplot as plt
import numpy as np

#xpoints = np.array([0, 6])
#ypoints = np.array([0, 250])

#plt.plot(xpoints, ypoints, 'o')

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([6, 2, 7, 11])

x1 = np.array([0, 1, 2, 3])
x2 = np.array([0, 1, 2, 3])
x3 = np.array([0, 1, 2, 3])


plt.subplot(1, 3, 1)
#plt.plot(x1, y1)
colors = ['red', 'blue', 'black', 'cyan']
#plt.scatter(x1, y1, color='hotpink')
plt.scatter(x1, y1, c=colors)
plt.title("estimated next month")
#the figure has 1 row, 3 columns, and this plot is the first plot.

plt.subplot(1, 3, 2)
ax=plt.gca()
plt.plot(x2, y2)
plt.colorbar(ax=ax)
plt.title("this month")
#the figure has 1 row, 3 columns, and this plot is the second plot.

plt.subplot(1, 3, 3)
plt.plot(x3, y3)
plt.title("last month")
#the figure has 1 row, 3 columns, and this plot is the third plot.

plt.suptitle("My Income")
#plt.colorbar()
plt.show()

