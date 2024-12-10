import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(2,8,100)
y = np.linspace(0, 5,100)
X, Y = np.meshgrid(x, y)

Z = (1/4) * np.sin((1/2) * X**2 - Y) - np.exp(-((X - 5)**2 + (Y - 2)**2))

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)

ax.view_init(30, 60)

plt.show()  