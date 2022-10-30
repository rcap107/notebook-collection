import numpy as np
import matplotlib.pyplot as plt

x_start, y_start = 0, 0

n_iter = 1000
n_runs = 20

x_coord = np.arange(n_iter)
y_coord = np.zeros(n_iter)

for run in range(n_runs):
    for it in range(1, n_iter):
        # x_coord[it] = x_coord[it - 1] + np.random.randn()
        y_coord[it] = y_coord[it - 1] + np.random.randn()        
    plt.plot(x_coord, y_coord)
plt.show()

