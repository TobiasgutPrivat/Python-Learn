import numpy as np
import pylab as pl
# Number of calculated points
n = 256
# create array of start values
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
#Calcs array of sin and cos values
Ysin = np.sin(2 * X)
Ycos = np.cos(2 * X)
#defines the individual lines, with data, color etc.
pl.plot(X, Ysin, color='blue', alpha=1.00)
pl.plot(X, Ycos, color='green', alpha=1.00)
#Width and height of displayed coordsystem
pl.xlim([-np.pi, np.pi])
pl.ylim([-2.5, 2.5])
#show plot
pl.show()
