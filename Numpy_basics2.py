import numpy as np
array_a=[1,2,3]
print(np.full_like(array_a,4))
#repeat
array_r=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,3,axis=1)
print(array_repeat)

array_zeros=np.zeros((5,5))
array_zeros[1,1]=7
print(array_zeros)

updated_array=np.zeros((7,7))
updated_array[1:-1,1:-1]=array_zeros
print(updated_array)
#copying arrays
array_x=np.array([1,2,3,4])
array_y=array_x
array_y[0]=28
print(array_y)
print(array_x)

#math operations

array_math=np.array([1,5,6])
'''print(array_math**2)
print(array_math-10)
print(array_math*2)'''
print(np.sin(array_math))
arr_a=np.ones([2,3])
arr_b=np.full([3,2],2)
print(np.matmul(arr_b,arr_a))



# copying arrays

array_x = np.array([1,2,3,4])

array_y = array_x

array_y[0] = 7

print(array_x)
print(array_y)



array_x = np.array([3,5,6,7])

array_y = array_x.copy()

array_y[0] = 10

print(array_x)
print(array_y)


# math operations

array_math = np.array([1,2,3])

print(np.sin)

print("Declared array: {}".format(array_math))
print("Add 10 to  array: {}".format(array_math + 10))
print("sub to from array: {}".format(array_math - 10))
print("raise to pow array: {}".format(array_math ** 2))
print("mul array by 5: {}".format(array_math * 5))
print("div array by 2: {}".format(array_math / 2))


# Algerba with numpy


arr_a = np.ones((2,3))

arr_b = np.full((3,2), 2)
print(arr_b)
print(arr_a)
print(np.matmul(arr_b,arr_a))

# statistics
import numpy as np
n_a = [[1,1,1,1], [0,0,0,0,0,0,0]]
print(n_a)
array_stats = [[1,2,3], [4,5,-6]]
print(np.min(array_stats))
print(np.min(array_stats,axis=1))
print(np.max(array_stats))
print(np.max(array_stats,axis=1))
print(np.sum(array_stats),axis=1)

# reshape
array_stats =np.array( [[1,2,3,7], [4,5,-6,4]])
print(array_stats.reshape((4,2)))

# stacking
a_v1 = np.array([1,2,3,4])
a_v2 = np.array([1,2,3,4])
print(np.array([a_v1, a_v2]))
print(np.hstack([a_v1, a_v2]))