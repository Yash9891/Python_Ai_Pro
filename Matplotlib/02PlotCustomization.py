import matplotlib.pyplot as plt
import numpy as np

# pyplot provieds a  userfriendly interface for ploting

# print(matplotlib.__version__)

x=np.array([2010,2015,2016,2024,2025,2026])
y=np.array([23,45,37,69,23,43])
y2=np.array([17,55,87,29,23,93])
y3=np.array([12,51,45,9,21,25])

line_style=dict(marker=".", markersize=20,
         markerfacecolor="black",
         markeredgecolor="red",
         linestyle='solid', #linestyle='none'- no line
        linewidth=3,
        #color="red"
        )
plt.plot(x,y,color="green",**line_style) #** unpack dict
plt.plot(x,y2,color="red",**line_style)
plt.plot(x, y3, color="blue", **line_style)

plt.show()