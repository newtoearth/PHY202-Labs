import numpy as np
import matplotlib.pyplot as plt 

halft = 3.053*60
dt = 1
tt = 500
f = lambda t: (-halft/np.log(2))*np.log(1-t)

for i in range(5):
	nTl = 500
	nPb = 0
	time = []
	for t in range(tt):
		r = np.random.rand()
		time.append(f(r))
	time = sorted(time)
	Tl = range(500,0,-1)
	Pb = range(0,500,1)
	plt.plot(time,Tl)
	plt.plot(time,Pb)
plt.show()