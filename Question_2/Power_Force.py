import matplotlib
from matplotlib import pyplot as plt
import math

def get_P(t):
    L = (200*(10-t))**0.5
    w = 0.2
    e = math.log(10/t)
    Y_avg_bar = 1.15*(530*e**1.26)/1.26
    mu = 0.1
    h_avg = (10+t)/2
    F = L*w*Y_avg_bar*(1+mu*L/2/h_avg)
    N = 200
    P = math.pi*F*L*N/60000
    return P

def get_F(t):
    L = (200*(10-t))**0.5
    w = 0.2
    e = math.log(10/t)
    Y_avg_bar = 1.15*(530*e**1.26)/1.26
    mu = 0.1
    h_avg = (10+t)/2
    F = L*w*Y_avg_bar*(1+mu*L/2/h_avg)
    return F
x = [8, 6, 3, 2] 

Fs = [get_F(i) for i in x]
y = [get_P(i) for i in x]
print(y)
plt.plot(Fs, y, color='green', marker='o', linestyle='solid')
plt.title('Question 2')
plt.xlabel('roll Force')
plt.ylabel('Power')
plt.show()
