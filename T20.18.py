
import numpy as np
import numpy.random as rnd

N = 10000

x = rnd.randint(1, 7, size=(N, 4))

s = np.sum(x, axis=1)
print(s)


k = len(s[s <= 9])

Wins = k * 10 / N

print(Wins)