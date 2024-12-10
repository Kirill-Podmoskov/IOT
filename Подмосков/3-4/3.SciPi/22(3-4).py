import numpy as np
import matplotlib.pyplot as plt

xmax, ymax = 1, 1
dx,dy = 0.01, 0.01
x,y = np.arange(0, xmax, dx), np.arange(0, ymax, dy)

f0x = 10
f0y = 20
fx = np.sin(2 * np.pi * f0x * x) + np.sin(2 * np.pi * 2 * f0x * x)
fy = np.sin(2 * np.pi * f0y * y) + np.sin(2 * np.pi * 2 * f0y * y)
I = np.tensordot(fx, fy, axes = 0)

X,Y = np.meshgrid(x,y)
plt.figure(figsize = (7,6))
plt.pcolor(X, Y, I, cmap = 'inferno')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()

noise = 4 * (2 * np.random.random_sample((x.size, y.size)) - 1)
plt.figure(figsize = (7,6))
plt.pcolor(X, Y, I + noise, cmap = 'inferno')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()

fI = np.fft.fft2(I + noise)
freqx = np.fft.fftfreq(x.size, dx)
freqy = np.fft.fftfreq(y.size, dy)
Lx = np.arange(1, np.floor(x.size/2), dtype = int)
Ly = np.arange(1, np.floor(x.size/2), dtype = int)

Spectrum = np.abs(fI) / x.size / y.size
Fx, Fy = np.meshgrid(freqx[Lx], freqy[Ly])

plt.figure(figsize = (6,5))
plt.title('Spectrum Weight', fontsize = 16)
plt.pcolor(Fx, Fy, Spectrum[Lx][:, Ly])
plt.xlabel('$f_x$', fontsize = 16)
plt.ylabel('$f_y$', fontsize = 16)
plt.colorbar()
plt.show()

ind = Spectrum > 0.1
I_filtered = np.fft.ifft2(fI * ind)
plt.figure(figsize = (7,6))
plt.pcolor(X, Y, I_filtered.real, cmap = 'inferno')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar()
plt.show()