import numpy as np
#list working
list_a=[1,2,3,4]
list_b=[5,6,7,8]
#print(list_a*list_b)
numpy_a=np.array([1,2,3,4])
numpy_b=np.array([5,6,7,8])
print(numpy_a * numpy_b)

#commom properties
numpyBasic_array=np.array([1.876,2,3,4])
#if there is atleast one float value in list then the item size is 8
#float----8
#int----4
#char----128_

print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize)
print(numpyBasic_array.size)

#2d Arrays
array_2D=np.array([[1,2,3],[7,3,7],[9,6,5]])
array_2D=np.array([[1*2*3],[4*5*6],[7*8*9]])
print(array_2D)
print("Dimensions:{}".format(array_2D.ndim))
print("Shape:{}".format(array_2D.shape))
print("Array Dtype:{}".format(array_2D.dtype))

array_2D=np.array([1,2,3],dtype='float64')
print(array_2D)
print(array_2D.itemsize)
print(array_2D.dtype)


#accessing array
array_x=np.array([[1,2,3,4,5],[7,3,7,7,9]])
print(array_x)
print(array_x.size)
print(array_x[1,2])
print(array_x[0,2])
print(array_x[:,2])
print(array_x[1])
print(array_x[0])

#step - [start:end:stepsize]
print(array_x[0,0:4:2])
print(array_x[:,0:4:2])
print(array_x[1,0:4:2])
array_x[0,2] = 10
array_x[:,2]=10
print(array_x)

#3d array
array_3d=np.array([[[1,2,3],[3,5,7]],[[6,9,0],[4,9,6]]])
print(array_3d)
print(array_3d[0,1,0])
array_3d[:,0, :]=100
print(array_3d)

array_3d=np.array([[[1,2,3],[4,9,6]]])
print(array_3d)
print(array_3d.shape)
#3d displays (objects,rows,columns)

array_3d=np.array([[[1,2,3],[3,5,7]],[[6,9,0],[4,9,6]]])
print(array_3d)
print(array_3d[:,0, :])
array_3d[:,0, :]=[[2,28,12],[4,19,7]]
print(array_3d)

#commom arrays
#one's two's empty

print(np.zeros(3))
print(np.ones(3))
two_d=np.zeros((2,3,3))
print(two_d)

three_d=np.zeros((2,3,3))
print(three_d)


four_d=np.zeros((2,3,3,2),dtype='int32')
print(four_d)
print(np.zeros(3,3))
print(np.full((3,3),[1,2,8]))


array_a=[1,2,3]
print(np.full_like(array_a,4))
#repeat
array_r-[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,2)
print(array_r)