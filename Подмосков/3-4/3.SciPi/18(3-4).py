import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, differential_evolution
import warnings
warnings.filterwarnings("ignore")

def gauss(z, sigma, x0, y0):
 x, y = z
 return np.exp(-((x-x0)**2 + (y-y0)**2) / sigma**2)

neg_gauss = lambda z, sigma, x0, y0: -gauss(z, sigma, x0, y0)

x = np.linspace(-20, 20, 100)
y = np.linspace(-20, 20, 100)
X, Y = np.meshgrid(x, y)
Z = gauss((X, Y), 100, 0, 0)
def mixed(z, *args):
 return np.sum(neg_gauss(z, *params) for params in args)
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
fig, ax = plt.subplots(1, 1, figsize=(8, 8))
contours = ax.contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax.clabel(contours, inline=True, fontsize=16)
contours = ax.contourf(X, Y, Z, 200, cmap=plt.cm.jet)
plt.show()

def get_path(xc):
 global path
 path.append(xc)

x0 = (-10, -2)
path = [x0]
result = minimize(mixed, x0,
 args=((10, -5, -12), (7, 5, 5), (9, -5, 10)),
 callback=get_path,
 )
Z = mixed((X, Y), (10, -5, -12), (7, 5, 5), (9, -5, 10))
path = np.array(path)
fig, ax = plt.subplots(1, 2, figsize=(20, 10))
contours = ax[0].contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax[0].clabel(contours, inline=True, fontsize=16)
contours = ax[0].contourf(X, Y, Z, 200, cmap=plt.cm.jet)
ax[0].scatter(path[:, 0], path[:, 1], s=1600, c='yellow',
 marker='*',
 alpha=1,
 edgecolor='black',
 linewidth=2,
 zorder=1)
ax[0].set_title('Gradient')

path = [x0]

def get_path(xc, convergence=0):
 global path
 path.append(xc)
result = differential_evolution(mixed, ((-20, 20), (-20, 20)),
 init=np.array([x0, (-9, -1), (-11, -3), (-8,
0), (-12, -4)]),
 args=((10, -5, -12), (7, 5, 5), (9, -5, 10)),
 recombination=0.15,
 seed=2,
 callback=get_path
 )
path = np.array(path)
contours = ax[1].contour(X, Y, Z, 16, colors="black", linewidths=2,
linestyles='-.')
ax[1].clabel(contours, inline=True, fontsize=16)
contours = ax[1].contourf(X, Y, Z, 200, cmap=plt.cm.jet)
ax[1].scatter(path[:, 0], path[:, 1], s=1600, c='yellow',
 marker='*',
 alpha=1,
 edgecolor='black',
 linewidth=2,
 zorder=1
 )
ax[1].set_title('DE')
plt.show()
