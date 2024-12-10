import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

func = lambda y, t: t**2
dt=1e-3
t = np.arange(0,1,dt)
res = odeint(func, y0 = 0, t = t)
plt.figure(figsize=(5,4))
plt.plot(t, res)
plt.plot(t[::50], t[::50]**3/3, 'o')
plt.show()
