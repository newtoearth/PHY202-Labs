import numpy as np
import matplotlib.pyplot as plt

f = lambda x : x**2 - 5

def graph():
	x = np.arange(-9,9,0.1)
	y = f(x)
	plt.plot(x,y)
	plt.plot(x,zeros(len(x)))
	plt.show()

def b_root(f,a,b):
	while(abs(b-a) > 0.00000001):
		if b < a:
			a,b = b,a
		t = (a + b) / 2
		if f(t) == 0:
			break
		elif f(t)*f(b) < 0:
			a = t
		elif f(a)*f(t) < 0:
			b = t
		else:
			break
	return t

x0 = b_root(f,-1,3)
print(x0)