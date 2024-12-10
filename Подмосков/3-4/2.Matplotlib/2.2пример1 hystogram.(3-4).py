import numpy as np
import matplotlib.pyplot as plt

y = np.random.standard_cauchy(size=10**7)

plt.hist(y, range=(0, 5), bins=50, density=True)
plt.title('Гистограмма распределения Коши')
plt.xlabel('Значения')
plt.ylabel('Плотность вероятности')
plt.grid()
plt.show()
