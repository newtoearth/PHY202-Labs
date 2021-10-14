import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0.0,100.0,25)
y = np.random.uniform(0.0,100.0,25)
y_err = np.random.uniform(0.0,1.0,25)

def linear_fit(x,y,y_err):
	exp_xy = 0
	exp_y = 0
	exp_x = 0
	exp_x2 = 0
	w = 0
	for i in range(len(x)):
		exp_xy += x[i]*y[i]/(y_err[i]**2)
		exp_x += x[i]/(y_err[i]**2)
		exp_y += y[i]/(y_err[i]**2)
		exp_x2 += (x[i]**2)/(y_err[i]**2)
		w += 1/(y_err[i]**2)
	exp_xy /= w
	exp_x /= w
	exp_y /= w
	exp_x2 /= w
	a = (exp_xy - exp_x*exp_y)/(exp_x2 - exp_x**2)
	b = exp_y - a*exp_x
	return a,b

x_ = np.linspace(0.0,100.0,25)
m,c = linear_fit(x,y,y_err)
y_ = m*x_ + c
plt.scatter(x,y)
plt.plot(x_,y_)
plt.show()