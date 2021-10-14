import numpy as np 
import matplotlib.pyplot as plt
import math

f = lambda x : math.sin(x) + math.sin(math.pi*x) + math.sin(x*math.exp(1))
x = np.arange(0,100,0.1)
y = list(f(xi) for xi in x)

plt.plot(x,y)
plt.show()

FT = np.fft.fft(y)/len(y)
freq = np.fft.fftfreq(len(x))
plt.plot(freq,abs(FT))
plt.show()