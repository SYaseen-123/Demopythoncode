import numpy as np
data_from_text_file=np.genfromtxt('Numpy_Dummy.txt',delimiter=',')
print(data_from_text_file)
print(data_from_text_file>10)

#advance indexing
print(data_from_text_file[data_from_text_file>10])


# fill values

fill_values = np.genfromtxt('Numpy_Dummy.txt' ,delimiter= ',', dtype=np.int32)
print(fill_values)
fill_values = np.genfromtxt('Numpy_Dummy.txt' ,delimiter= ',', dtype=np.int32, filling_values = 100)
print(fill_values)

def numpy_function(x,y):
    return 10 * x+y
b = np.fromfunction(numpy_function, (4,5), dtype='int32')
print(b)

 