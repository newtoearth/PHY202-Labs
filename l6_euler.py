import numpy as np
f = lambda x,y: np.cos(x)

def euler(f,y0,t):
	x0 = 0
	y = y0
	h = t/100
	while t > x0:
		y += h * f(x0,y)
		x0 += h
	return y

y_t = euler(f,0,0.1)
print(y_t)