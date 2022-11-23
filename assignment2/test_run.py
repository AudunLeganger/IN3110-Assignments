from array_class import Array
import numpy as np
arr1 = Array((3,2),1,2,3,5,2,5)
arr2 = Array((3,),2,5,8)
lst = []
np_arr = np.array([[1,2,3],[4,5,6]]) #2,3
print(np_arr.tolist())
np_arr_3d = np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]],[[13,14,15],[16,17,18],[19,20,21],[22,23,24]]])
print(np_arr_3d.tolist()) #
