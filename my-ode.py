import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


# function that returns dy/dt
def model(y,x):
    k = 1
    q = 1
    x1 = 5
    y1 = 2
    
    dydt = (k*q*(y-y1)/((x-x1)**2 + (y-y1)**2)**(3/2))/(k*q*(x-x1)/((x-x1)**2 + (y-y1)**2)**(3/2))
    

    return dydt



# time points
x = np.linspace(0,20,200)

# solve ODE
y1 = odeint(model,8,x)
y2 = odeint(model,5,x)


# plot results
plt.plot(x,y1)
plt.plot(x,y2)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()