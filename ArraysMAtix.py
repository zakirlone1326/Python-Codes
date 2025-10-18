#creating array
import numpy as np
array=np.array([1,2,3,4,5])
print("Array: ", array)
print(array[2]) #access by index

#operations on arrys
import numpy as np
array1=np.array([1,2,3])
array2=np.array([4,5,6])

print("sum of arrays is: ",array1+array2)
print("product of arrays :", array1*array2)
print("difference : ", array1-array2)
print("Division: ",array1/array2)
scalar=5 #can be taken any value
broadcast_array= array1+scalar #will add 5 to array 1
print("Array after broadcsting : ",broadcast_array)

#creating matrix --->  matrix is 2d aray
import numpy as np

matrix=np.array([[1,2,3],[4,5,6]])
print("matrix: \n", matrix)
