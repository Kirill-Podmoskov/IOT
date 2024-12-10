import numpy as np
import matplotlib.pyplot as plt
import random

#В примере неправильный график для этой функции
#https://www.wolframalpha.com/input?i2d=true&i=sinx+%2B+tg%5C%2840%292%5C%2840%29x-2%5C%2841%29%5C%2841%29 - как выглядит по настоящему функция
x = np.linspace(-5, 5, 40)
y = np.sin(x) + np.tan(2 * (x - 2))

yerr = [random.uniform(1, 2) for _ in range(len(x))]

plt.figure(figsize=(10, 5))
plt.errorbar(x, y,
             yerr=yerr,
             ecolor='forestgreen',  # Цвет ошибок
             capsize=10,  # Ширина
             linewidth=1.5)  # Толщина

plt.title('График функции с погрешностями')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid()
plt.show()