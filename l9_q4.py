import numpy as np
import matplotlib.pyplot as plt

num4 = np.random.rand(500)
for _ in range(99):
	num4 += np.random.rand(500)

plt.hist(num4)
plt.show()