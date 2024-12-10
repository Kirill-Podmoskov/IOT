import numpy as np
import matplotlib.pyplot as plt

x_min = -2 * np.pi
x_max = 2 * np.pi
num_points = 100
x = np.linspace(x_min, x_max, num_points)

fig, ax = plt.subplots(2, 2, figsize=(8, 6))

ax[0, 0].plot(x, np.sin(x))
ax[0, 0].set_title("sin(x)")
ax[0, 0].set_xlabel("x")
ax[0, 0].set_ylabel("y")

ax[0, 1].plot(x, np.sin(x / 2))
ax[0, 1].set_title("sin(x/2)")
ax[0, 1].set_xlabel("x")
ax[0, 1].set_ylabel("y")

ax[1, 0].plot(x, np.cos(x))
ax[1, 0].set_title("cos(x)")
ax[1, 0].set_xlabel("x")
ax[1, 0].set_ylabel("y")

ax[1, 1].plot(x, np.cos(x / 2))
ax[1, 1].set_title("cos(x/2)")
ax[1, 1].set_xlabel("x")
ax[1, 1].set_ylabel("y")

plt.tight_layout()
plt.show()