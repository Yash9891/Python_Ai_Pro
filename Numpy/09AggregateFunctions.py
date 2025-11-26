import numpy as np

#aggregate func- sumarize data and return  a single value

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array)) #standard deviation fun
# print(np.var(array)) # variance
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))# position of min value
# print(np.argmax(array))# position of max value

#Sum of columns
print(np.sum(array,axis=0))  

#sum of rows
print(np.sum(array, axis=1))