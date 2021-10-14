import numpy as np
import matplotlib.pyplot as plt

for i in range(5):
	nTl = 100
	nPb = 0
	halft = 3.053*60
	dt = 1
	tt = 2000
	p = 1-2**(-dt/halft) #Nt/NT
	time = np.arange(0.0,tt,dt)
	Tl = []
	Pb = []
	for dt in time:
		Tl += [nTl]
		Pb += [nPb]
		d = 0
		for i in range(nTl):
			r = np.random.rand()
			if r < p:
				d += 1
		nTl -= d
		nPb += d

	plt.plot(time,Tl)
	plt.plot(time,Pb)
plt.show()