import numpy as np

N = 50000
x = list(np.random.rand(N))
f = lambda x : ((1-x**2)**0.5)
y = (f(x[i]) for i in range(N))
s = sum(y)
pi = 4 * s / N
print(pi)