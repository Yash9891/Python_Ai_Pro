import numpy as np

#comparision operators

scores=np.array([91,55,100,73,82,64])

print(scores==100)
print(scores>=60)

#assign 0 if <60

scores[scores<60]=0
print(scores)