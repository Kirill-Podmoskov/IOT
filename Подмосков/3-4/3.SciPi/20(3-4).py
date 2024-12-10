from scipy.optimize import minimize
import numpy as np

def f(z, a, b):
  x, y = z
  return (x + y)**2 - 2 * x * (y + a) - 2 * y * b + a + b
a = 0
b = 0

x0 = np.array([0, 0])  

result = minimize(f, x0, args=(a, b))

x_min, y_min = (result.x)
x_min_r = round(x_min, 2)
y_min_r = round(y_min, 2)

print(f"Координата x минимума: {x_min_r}")
print(f"Координата y минимума: {y_min_r}")