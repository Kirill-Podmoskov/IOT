import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def func(y, t):
    u, f = y
    dydt = [2 * u - f, u]
    return dydt

y0 = [1, 1]

t = np.linspace(0, 10, 1000)

res = odeint(func, y0, t)

f_values = res[:, 1]

plt.plot(t, f_values, label='f(t)')
plt.plot(t[::50], np.exp(t[::50]), 'o', label='exp(t)', markersize=5)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.legend()
plt.show()
