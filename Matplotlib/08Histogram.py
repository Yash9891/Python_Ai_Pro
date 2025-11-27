import matplotlib.pyplot as plt
import numpy as np

# histogram - a visual replresentation of the distribution of quantitive data.
# they group values into bins(intervals)
#and counts how many fall in each range


#loc= location - median- 80 is the student score most is 80 and scale means how far the score will deviate from 80- 10 is standard deviation( if 1 is there then scores will cluster around 80 most)
scores=np.random.normal(loc=80, scale=10, size=100)
scores=np.clip(scores, 0, 100)# range of score min=0 and max=100
plt.hist(scores, bins=10, color="lightgreen",
         edgecolor="green") # 10 nins= 10 bar

plt.title("Exam Scores")
plt.xlabel("Score")
plt.ylabel("No of students")

plt.show()
