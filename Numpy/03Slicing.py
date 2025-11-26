import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

#array[start:end:step]

# print(array[0:])

# print(array[0::2]) #step

# print(array[:,0])  # select each row with col1 
# print(array[:,-1])
# print(array[:,0::2]) #:,  selectet each row 

# 1st 2 rowa and first 2 col

print(array[0:2,0:2])  #[0:2,0:2]=[0 to 1 rows, 0 to 1st col]

print(array[2:, 2:])