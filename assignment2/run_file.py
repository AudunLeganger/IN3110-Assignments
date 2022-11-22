from array_class import *

array1 = Array((3,), 1,2,3)
array2 = Array((3,), 5, 7, 3)
print(array1.is_same_shape(array2))
print(array1*array2)