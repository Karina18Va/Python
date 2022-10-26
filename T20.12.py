import numpy as np
def matrix1(q):
    n = True
    for i in range(q.shape[1]):
        if np.sum(q[:, i][i+1:]) != 0:
            n = False
            break
        if n:
            print("Матриця верхня трикутна")
        else:
            print("Матриця не верхня трикутна")

def matrix2(w):
    m = True
    for i in range(w.shape[1]):
        if np.sum(w[:i, ][:i+1, ]) != 0:
            m = False
            break
        if m:
            print("Матриця нижня трикутна")
        else:
            print("Матриця не нижня трикутна")


if __name__ == "__main__":
    q = np.array([[3, 4, 5], [0, 0, 0], [0, 0, 0]])
    print(matrix1(q))
    w = np.array([[0, 0, 0], [0, 0, 0], [8, 9, 6]])
    print(matrix2(w))


