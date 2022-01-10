import matplotlib
from matplotlib import pyplot as plt
import math


x = [8, 6, 3, 2]
l = 10
y = [math.log(l/i) for i in x]
print(y)
plt.plot(x, y, color='green', marker='o', linestyle='solid', label= "true strain")
plt.title('Question 2')
plt.xlabel('thickness')
plt.ylabel('true strain: ln(l / lo)')
plt.show()
