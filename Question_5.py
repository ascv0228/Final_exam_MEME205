import matplotlib
from matplotlib import pyplot as plt
import math

x = range(5,30,5)
def get_Y(r,x):
    Y = 1/(4*(r*x)**3-3*r*x+1)
    return Y

Y_E = [90/73e3, 210/73e3, 265/127e3, 265/195e3]

print(Y_E)
y = [get_Y(Y_E[0], i) for i in x]
plt.plot(x, y, color='green', marker='o', linestyle='solid', label="5052-O-Al")
y = [get_Y(Y_E[1], i) for i in x]
plt.plot(x, y, color='blue', marker='o', linestyle='solid', label="5052-H34-Al")
y = [get_Y(Y_E[2], i) for i in x]
plt.plot(x, y, color='aqua', marker='o', linestyle='solid', label="C24000-Brass")
y = [get_Y(Y_E[3], i) for i in x]
plt.plot(x, y, color='orange', marker='o', linestyle='solid', label="AISI-304-SS")
plt.title('Question 5')
plt.xlabel('Ri/t')
plt.ylabel('Rf/Ri')
plt.legend()
plt.show()
