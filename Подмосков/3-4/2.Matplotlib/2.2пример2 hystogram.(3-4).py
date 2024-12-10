import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(-5*np.pi, 5*np.pi, size=10**7)  # выборка 10^7

y1 = np.random.normal(loc=-10, scale=7, size=len(x))
y2 = np.random.normal(loc=10, scale=5, size=len(x))
y3 = np.random.normal(loc=25, scale=10, size=int(1.5 * len(x)))

y = np.concatenate((y1, y2, y3))

plt.hist(y, bins=100, alpha=0.7)
plt.title('Гистограмма смешанных нормальных распределений')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid()
plt.show()
