import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def bio_sys(y, t, a, b):
    y0, y1 = y
    dydt = [a*(y0 - y0*y1), b*(-y1 + y0*y1)]
    return dydt
    
a = 1.0
b = 0.2
initial_y0 = 0.1
initial_y1 = 1.0
initial_y = [initial_y0, initial_y1]

t = np.linspace(0,5,150)
sol_p1 = odeint(bio_sys, initial_y, t, args=(a,b))

#Plot of y0 and y1 against t
plt.plot(t, sol_p1[:, 0], 'b', label='y0(t)')
plt.plot(t, sol_p1[:, 1], 'g', label='y1(t)')
plt.title('Plot of y against t with y0(0)=0.1')
plt.legend(loc='best')
plt.xlabel('t (Year)')
plt.ylabel('y')
plt.grid()
plt.savefig('plot_of_y_against_t_p1.jpg')
plt.show()

# plotting the graph for y1 against y0
plt.plot(sol_p1[:, 0],sol_p1[:,1], 'b')
plt.title('Graph of y1 against y0 with y0(0) = 0.1')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('plot_of_y1_against_y0_p1.jpg')
plt.show()

"""
PART 2
"""


initial_y0 = 0.11
initial_y1 = 1.0
initial_y = [initial_y0,initial_y1]
sol_p2 = odeint(bio_sys, initial_y, t, args=(a,b))

#Graph of y0 and y1 against t
plt.plot(t, sol_p2[:, 0], 'b', label='y0(t)')
plt.plot(t, sol_p2[:, 1], 'r', label='y1(t)')
plt.title('Graph of y0 and y1 against t with y0(0)=0.11')
plt.legend(loc='best')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.savefig('plot_of_y_against_t_p2.jpg')
plt.show()

plt.plot(sol_p2[:, 0],sol_p2[:,1], 'r')
plt.title('Graph of y1 against y0 with y0(0) = 0.11')
plt.xlabel('y0')
plt.ylabel('y1')
plt.grid()
plt.savefig('plot_of_y1_against_y0_p2.jpg')
plt.show()
