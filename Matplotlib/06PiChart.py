# Pi chart is a circular chart divided into slices to show percentage of the total.
# good for visualization distribution among categories
import matplotlib.pyplot as plt
import numpy as np

categories=["Freshmen", "sophomores", "Juniors", "seniors"]
values=np.array([300, 250, 275, 225])
colors=["red", "yellow", "skyblue", "orange"]
plt.pie(values, labels=categories,
        autopct="%1.1f%%", # percentage
        colors=colors,
        explode=[0,0,0,0.1],# higlight pi slice
        shadow=True,
        startangle=180)

plt.title("Godzilla college")
plt.show()