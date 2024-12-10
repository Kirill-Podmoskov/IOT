import numpy as np
import matplotlib.pyplot as plt

fi = np.linspace(0,2*np.pi,100)
tau = np.linspace(0,2*np.pi,100)

FI, TAU = np.meshgrid(fi, tau)

X = (10+8*np.cos(FI))*np.cos(TAU)
Y = (10+8*np.sin(FI))*np.sin(TAU)
Z = 8*np.sin(FI)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")

ax.plot_surface(X, Y, Z, cmap=plt.cm.ocean_r)

ax.view_init(30, 60)

plt.show()  