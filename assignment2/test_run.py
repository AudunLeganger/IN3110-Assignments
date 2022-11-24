from array_class import Array
import numpy as np
arr1 = Array((3,2),1,2,3,5,2,5)
arr2 = Array((3,),2,5,8)
arr3 = Array((2,3,2),1,2,3,4,5,6,7,8,9,10,11,12)
'''
arr_2d =np.zeros([3,5])
print(arr_2d)
print(arr_2d.tolist())
print("-------------------")
arr_3d = np.zeros([4,3,2])
#print(arr_3d)
#print(arr_3d.tolist())
# np_arr_3d = np.zeros([4,3,2])
#print(np_arr_3d)
'''
multi_list = arr3.values
#print(list(arr3.flatten_list(multi_list)))
print(arr3)
print(arr3[1][1][0])