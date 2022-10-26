import numpy as np

import numpy.random as rnd

N = 1000
x = rnd.uniform(-1, 1, N)
y = rnd.uniform(-1, 1, N)

z = np.array(x**2 + y**2 <= 1)
k = z[z == 1]

PI = k.size()/N * 4

print("pi {}".format(PI))
