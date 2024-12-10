import numpy as np
import matplotlib.pyplot as plt

x_min = -10
x_max = 10
num_points = 1000

x = np.linspace(x_min, x_max, num_points)
y = np.sin(2 * x) ** 2 * np.exp((x + 2) / 10) ** 2

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("График функции y(x) = sin^2(2x)e^((x+2)/10)^2")
plt.grid(lw=0.5, ls='--')
plt.plot(x,y, lw = 4.0,color='red')
plt.plot(x,y, lw = 5.0, color='black', zorder=0)
plt.show()