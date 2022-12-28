import numpy as np
n_a = [[1,1,1,1], [0,0,0,0,0,0,0]]
print(n_a)
array_stats = [[1,2,3], [4,5,-6]]
print(np.min(array_stats))
print(np.min(array_stats,axis=0))
print(np.min(array_stats,axis=1))
print(np.max(array_stats))
print(np.max(array_stats,axis=0))


# reshape
array_stats =np.array( [[1,2,3,7], [4,5,-6,4]])
print(array_stats.reshape((4,2)))

three_d=np.arange(24).reshape(2,3,4)
print(three_d)
print(three_d.shape)

four_d=np.arange(48).reshape(2,2,3,4)
print(four_d)
print(four_d.shape)


import numpy as np
array_one=np.array([[1,2],[3,4]])
array_two=np.array([[5,6],[7,8]])
print(array_one * array_two)
import numpy as np
#numpy as a list
array_l=np.array([1,2,3,4,5,6,7,8,9,8,7,6])
#numpy arrays can be indexed as a list
print(array_l[[1,3,5,3]])


