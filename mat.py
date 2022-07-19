import matplotlib.pyplot as plt

#x = [1, 2, 3, 4, 5]
#y = [1, 4, 9, 16, 25]
#plt.plot(x, y, "r.")
#plt.show()
import numpy as np

dataY = []
def function1(x):
    return x * x

for i in range(1, 101):
    info = function1(i)
    dataY.append(info)
print(dataY)
plt.plot(np.arange(100), dataY)
plt.show()