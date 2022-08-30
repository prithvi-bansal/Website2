import matplotlib.pyplot as plt
import numpy as np

plt.plot([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], [25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25], 'D-.c', ms=5, mec='k', mfc='m')

# ls='None'
# 'D-.c' = marker|line|color
# ms = marker size
# mec = marker edge color
# mfc = marker face color

plt.axis([-6, 6, 0, 30])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Squares of numbers", fontdict=font1)
plt.ylabel('squares', fontdict=font2)
plt.xlabel('numbers', fontdict=font2)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
plt.show()


x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.subplot(2,2,1)
plt.bar(x,y, color='black', width=0.4)

plt.subplot(2,2,2)
plt.barh(x,y, color='hotpink', height=0.1)



x = np.random.normal(170, 10, 250)
plt.subplot(2,2,3)
plt.hist(x)


y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
plt.subplot(2, 2, 4)
plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.legend(title="Fruits")


plt.show()

