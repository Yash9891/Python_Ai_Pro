import numpy as np

array = np.array([["a", "b", "c"], 
                ["d", "f", "g"],
                ["g", "h", "i"]])

print(array.ndim)
print(array.shape)
print(array[0,2])
word=array[0,0]+array[1,2]+array[2,0]
print(word)
