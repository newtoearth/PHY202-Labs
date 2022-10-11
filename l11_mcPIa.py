import random

N = 50000
c = 0
s = 0
for i in range(N):
	pt = (random.uniform(-1,1),random.uniform(-1,1))
	d = pt[0]**2 + pt[1]**2
	if d <= 1:
		c += 1
	s += 1
pi = 4*(c/s)
print(pi)
