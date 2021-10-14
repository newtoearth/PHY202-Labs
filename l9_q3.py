import numpy as np
import matplotlib.pyplot as plt

num3 = np.random.rand(500)+np.random.rand(500)+np.random.rand(500)
plt.hist(num3)
plt.show()