from scipy.integrate import odeint
import numpy as np
f0 = float(input())
dt = 0.001
t = np.arange(0,1,dt)

def f(y, t):
  return y + t
res = odeint(f, f0, t)
f_at_1 = res[-1][0]
f_at_1_rounded = round(f_at_1, 2)

print(f"f(1) = {f_at_1_rounded}")