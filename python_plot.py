import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 2*np.pi, 100)

fig, ax = plt.subplots(figsize=(8,5))
ax.plot(x, x)
ax.set_xlim(0, 2*np.pi)
plt.show()
