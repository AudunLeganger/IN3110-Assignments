from array_class import *

array1 = Array((3,), 1,2,3)
# array2 = Array((3,), "Hei", "på", "3")
# array3 = Array((4,), False, False, True, True)

z1 = complex(1,3)
z2 = complex(4,2)
z3 = complex(-2,-10)
array2 = Array((3,),z1,z2,z3)
array3 = Array((3,), 5,10,9)
print(array2)

print(type(array1))
print(array1 + 10)
print(array1 + array3)
print(type(array1 + array3))
print(type(array1 + 10))
print(15 + array1)