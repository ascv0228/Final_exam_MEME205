import matplotlib
from matplotlib import pyplot as plt
import math

def get_F(k,R):
    F = math.pi*0.25*2/4*k*math.log(R)
    return F
ks = [350,400,450]
Rs = range(5, 51,5)
Fs = [get_F(ks[0],i) for i in Rs]
plt.plot(Rs, Fs, color='green', marker='o', linestyle='solid', label="900。C")
Fs = [get_F(ks[1],i) for i in Rs]
plt.plot(Rs, Fs, color='blue', marker='o', linestyle='solid', label="1000。C")
Fs = [get_F(ks[2],i) for i in Rs]
plt.plot(Rs, Fs, color='aqua', marker='o', linestyle='solid', label="1100。C")
plt.title('Question 2')
plt.xlabel('extrusion ratio (R)')
plt.ylabel('F')
plt.legend()
plt.show()
