import matplotlib.pyplot as plt
import numpy as np
import math
X = []
Y = []
x = 0
h = 0.1
while (x<4):
    x=x+h
    X.append(x)
    y = 4*math.cos(x)-3*math.sin(x)+2*(x*x)+2*x-4
    Y.append(y)

X1 = [0]
U = [0]
V = [-1.0]
x = 0
while (x<4):
        x = round(X1[-1], 2)
        u = U[-1]
        v = V[-1]
        k1 = h * v
        l1 = h * (2*x**2 + 2*x - u)
        
        k2 = h * (v + 0.5*l1)
        l2 = h * (2*(x + 0.5*h)**2 + 2*(x + 0.5*h) - (u + 0.5*k1))
        
        k3 = h * (v + 0.5*l2)
        l3 = h * (2*(x + 0.5*h)**2 + 2*(x + 0.5*h) - (u + 0.5*k2))
        
        k4 = h * (v + l3)
        l4 = h * (2*(x + h)**2 + 2*(x + h) - (u + k3))
        
        u2 = u + (k1 + 2*k2 + 2*k3 + k4) / 6
        v2 = v + (l1 + 2*l2 + 2*l3 + l4) / 6
        x2 = round(x + h, 2)
        
        X1.append(x2)
        U.append(u2)
        V.append(v2)

plt.plot(X1, U, 'b')
#plt.plot(X1, V, 'g')
plt.plot(X, Y, 'r--') 
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show() 
