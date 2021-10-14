import numpy as np
f = lambda x,y: np.cos(x)

def rk2(f,y0,t):
	x0 = 0
	y = y0
	h = t/100
	for i in range(1,101):
		k1 = h*f(x0,y)
		k2 = h*f(x0 + h,y + k1)
		y += (1.0/2.0)*(k1 + k2)
		x0 += h
	return y

y_t = rk2(f,0,0.1)
print(y_t)