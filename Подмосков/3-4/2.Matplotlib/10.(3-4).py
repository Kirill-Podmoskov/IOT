import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-4,4,100)
y = np.linspace(-4, 4,100)
X, Y = np.meshgrid(x, y)

Z = np.sin(X**2+Y**2)/(X**2+Y**2)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z / Z.max(), cmap=plt.cm.ocean_r)

ax.view_init(30, 60)

plt.show()  