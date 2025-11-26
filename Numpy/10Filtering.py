import numpy as np

#Filtering refers to the prpcess of selecting selements from array that match a given condition

ages=np.array([[21,17,18,19,20,65],[
                39, 22, 15,99,18, 19
]])

teenagers=ages[ages<18]  # one dimentional
adults=ages[(ages>=18) & (ages <=60)]
print(teenagers)
print(adults)

evens=ages[ages%2==0]
print(evens)

# Preserve original Dimention
adults=np.where(ages>=18,ages, 0 )  # replace NA with 0
print(adults)

