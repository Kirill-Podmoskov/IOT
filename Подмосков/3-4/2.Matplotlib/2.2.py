import numpy as np
import matplotlib.pyplot as plt

x_min = -3 * np.pi
x_max = 3 * np.pi
num_points = 250

x = np.linspace(x_min, x_max, num_points)
y = np.sin(x)
noise = np.random.normal(loc=1, scale=4, size=num_points) * 0.1
y_noisy = y + noise

plt.figure(figsize=(10, 5))

plt.scatter(x, y_noisy)

plt.scatter(x, y_noisy,
 s=300,
 marker='s',
 c='violet',
 lw=2,
 edgecolor='black',
 hatch='**'
 )

plt.title(
 label='$sin(x)$ with random noise', # Заголовок
 fontsize=20) # Размер шрифта)

plt.xlabel('x range', fontsize=18)

plt.ylabel('y range', fontsize=18)

plt.tick_params(labelsize=16)

plt.yticks(
 ticks=np.arange(-1.5, 2,0.5), 

 labels=['можно', 'написать', 'все', 'что', 'хочется', 'вообще', 'все ='][::-1]
)


