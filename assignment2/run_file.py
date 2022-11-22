from array_class import *

array1 = Array((3,), 1,2,3)
array2 = Array((3,), 5, 7, 3)
array3 = Array((4,), 1.3, 0.0, 2.5, 3.5)
array4 = Array((4,), 0.0, 1.0, 2.0, 3.0)
array5 = Array((3,), True, True, False)

print(array1 + 10)
print(15 + array1)
print(12.0 * array3)
print(array1 + array2)