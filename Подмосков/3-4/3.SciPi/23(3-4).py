import numpy as np
def find_max_frequency(v):
    t = np.linspace(0, 1, 1000)
    f_t = np.sin(v * np.cos(2 * np.pi * t))
    N = len(f_t)
    yf = np.fft.fft(f_t)
    T = t[1] - t[0]
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    idx_max = np.argmax(np.abs(yf[:N//2]))
    return xf[idx_max]

v = float(input())
max_frequency = find_max_frequency(v)
print(max_frequency)