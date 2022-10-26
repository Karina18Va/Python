import numpy as np
import numpy.random as rnd
N = 1000


def krap(n, win, loss, continuation):
    dots = np.random.randint(1, 7, n)
    value = np.sum(dots)
    if value in loss:
        return False
    elif value in win:
        return True
    else:
        our_value = value
        while True:
            dots = np.random.randint(1, 7, n)
            value = np.sum(dots)
            if value in continuation:
                return False
            elif value == our_value:
                return True


def probability_of_winning(n, win, loss, continuation):
    rez = np.zeros(N)
    for i in range(N):
        rez[i] = krap(n, win, loss, continuation)
    return np.sum(rez) / N


if __name__ == "__main__":
    a = probability_of_winning(2, (7, 11), (2, 3, 13), (7, ))
    print(a)