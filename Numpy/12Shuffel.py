import numpy as np

# rng=np.random.default_rng()
# array=np.array([1,2,3,4,5])
# rng.shuffle(array)
# print(array)

# select any 2 random fruits--------------------

fruits=np.array(["apple","mango","banana"])
rng=np.random.default_rng()
fruit=rng.choice(fruits, size=(2,3))
print(fruit)