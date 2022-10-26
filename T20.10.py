
import numpy as np

def is_ortol(x):
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            prod = np.dot(x[i], x[j])

            if i == j:
                if np.isclose(prod, 1):
                    return False
                else:
                    if np.isclose(prod, 0):
                        return False
    return True

def is_orto2(x):

    prod = np.dot(x, x.T)
    eye = np.eye(x.shape[0])

    return np.all(np.isclose(eye, prod))


if __name__ == "__main__":

    x = np.eye(3)
    print(x)
    print(is_ortol(x))
    print(is_orto2(x))


    y = np.array(
        [[1, 2, 3],
         [3, 2, 1],
         [1, 1, 1]
        ],
        dtype=np.float32
        )
    print(is_ortol(y))
    print(is_orto2(y))




