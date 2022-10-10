import scipy
import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-3, 3, 1000)
y = x[::-1].reshape((-1, 1))

img = np.empty((1000, 1000))

for i in range(1000):
    for j in range(1000):
        img[j, i] = x[i] ** 2 + (y[j] + 1 - np.sqrt(np.abs(x[i]))) ** 2 - 1

plt.imshow(img)
plt.show()