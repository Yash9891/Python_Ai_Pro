"""
Scatter graph= shows the relationship btw two variables
helps to indentify a correlation(+, -, None)
Ex- study hours vs Test scores
"""

import matplotlib.pyplot as plt
import numpy as np

x1=np.array([0,1,1,2,3,4,5,6,7,7,9]) # hours stydy
y1=np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87]) # grades

x2=np.array([0,1,2,2,3,4,5,6,7,8,8]) # hours stydy
y2=np.array([50, 60, 63, 68, 68, 70, 78, 78, 82, 95, 97]) # grades


plt.scatter(x1,y1, color="skyblue",
            alpha=0.6,
            s=100,
            label="Class A")
plt.scatter(x2,y2, color="orange",
            alpha=0.6,
            s=100,
            label="Class B")
plt.title("Test scores")
plt.xlabel("Hours studies")
plt.ylabel("Grades")
plt.legend()# to show poits label
plt.show()
