from scipy.optimize import minimize
import numpy as np

def f(x):
  return -x**2 * (x - 4)**2 * np.exp(-x**2)  
x0 = float(input())  
result = minimize(f, x0=x0)
x_max =  round(result.x[0],2)
print(x_max)