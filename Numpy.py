import numpy as np
import sys
# a = np.array([1,2.3], dtype='int32')
# b = np.array([[9.1,8.0,7.0],[6.0,5.0,4.0]])
# Get dimemsion a.ndim -> a.ndim = 1, b.ndim = 2
# b.shape -> (2,3): (number of children array and number of element)
# a.dtype
# a.itemsize
# a.nbytes = a.itemsize * a.size
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
# print(a[1][5])
# print(a[0,:])
# print(a[0, 5:0:-2])
# print(a[1,0]) -> a[i][j]
# b = np.zeros((2,3))
# b = np.full((2,2), 99)
# b = np.full_like(a,4)
# b = np.random.rand(4,2) -> random o thuc 0 <= 1
# b = np.random.randint(-4,8, size = (3, 3)) -> random so nguyen
# b = np.identity(5) -> ma tran don vi
# arr = np.array([[1,2,3]])
# r1 = np.repeat(arr,3,axis = 0)
# print(r1)
# arr = np.append(arr, [1])
# arr = np.insert(arr,1,99)
# print(arr1 ** 2)
arr1 = np.full((2,3), 1)
arr2 = np.full((3, 3), 2)
arr2[0,0:3] = 1
# print(np.matmul(arr1,arr2)) -> Matrix Mullitification
# np.linalg.det(arr2) -> find the determinant of arr2
# print(np.linalg.det(arr2))
# np.min(arr2), np.max(arr2)
# np.sum(arr2, axis = 0) -> total of every single column
# np.sum(arr2, axis = 1) -> total of every single row
# print(np.sum(arr2, axis = 1)) 
# before = np.array([[1,2,3,4],[5,6,7,8]])
# print(before)

# after = before.reshape((4,2))
# print(after)
# h1 = np.full((2,4),1)
# h2 = np.zeros((2, 2))
# print(np.hstack((h1,h2)))
filedata = np.genfromtxt('data.txt', delimiter=',')
filedata = filedata.astype('int32')
print(filedata)