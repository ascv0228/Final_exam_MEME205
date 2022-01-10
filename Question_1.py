import matplotlib
from matplotlib import pyplot as plt
import math

x = range(15, 91, 5)
alpha = [w / 180 * math.pi for w in x]
def get_F(mu):
    Y = 275
    Af=1.76714
    ratio = math.log(4.9087/1.76714)
    y = [Y*Af*((1+mu/a)*ratio + 2/3*a) for a in alpha]
    a = 15/180*math.pi
    print(Y*Af*((1+mu/a)*ratio + 2/3*a))
    return y
get_F(0.1)
mu =0.1
plt.plot(x, get_F(mu), color='green', marker='o', linestyle='solid',label=f'Friction={mu}')
mu =0.3
plt.plot(x, get_F(mu), color='blue', marker='o', linestyle='solid',label=f'Friction={mu}')
mu =0.5
plt.plot(x, get_F(mu), color='aqua', marker='o', linestyle='solid',label=f'Friction={mu}')
plt.title('Question 1')
plt.xlabel('degree')
plt.ylabel('F')
plt.legend()
plt.show()
