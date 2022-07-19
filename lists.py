import numpy as np
array = np.array( [[[1, 2],[1, 2]],[[1, 2],[1, 2]]])
print(array)
print(array.shape)

num1 = [1, 1, 1, 1, 1]
num2 = [1, 1, 1, 1, 1]
print(num1 + num2)
num3 = ([])
for x in range(len(num1)):
    num3.append(num1[x] + num2[x])
print(num3)

arr1 = np.array([1, 1, 1, 1, 1])
arr2 = np.array([1, 1, 1, 1, 1])
print(arr1 + arr2)

arr3 = np.array([1, 2, 3, 4, 5])
arr4 = np.array([2, 3, 4, 5, 6])
print(arr3+5)