# barchar compare categories of data by representing each category with a bar
import matplotlib.pyplot as plt
import numpy as np

categories=["Graines","Fruits", "vegetables","protein", "dairy", "sweets"]
values=np.array([4, 3, 2, 5, 3, 1] )

#bar chart
plt.bar(categories, values, color="skyblue")
#plt.barh(categories, values, color="skyblue")# horizontal barchart

plt.title("Daily consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()