import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
plt.plot(x, y)

x = np.linspace(0, 2 * np.pi, 1000)
y = np.sin(x) + np.cos(10 * x) + np.random.random(len(x))
plt.plot(x, y)
plt.xlabel("New Time")
plt.ylabel("Signal")
plt.show()


(print "Some other change for testing making puul reqeusts")