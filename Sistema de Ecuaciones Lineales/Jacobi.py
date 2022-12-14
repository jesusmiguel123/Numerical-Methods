import matplotlib.pyplot as plt
import numpy as np
import scipy.linalg as la

def Jacobi(A, b, x0, k):
    lx, le = [], []
    D = np.diag(np.diag(A))
    L, U = np.tril(A) - D, np.triu(A) - D
    x = x0
    for i in range(k):
        T = -np.dot(la.inv(D), L + U)
        c = np.dot(la.inv(D), b)
        x = np.dot(T, x) + c
        lx.append(x), le.append(la.norm(b - np.dot(A, x), 2))
    return lx, le

def JacobiParada(A, b, x0, tau):
    D = np.diag(np.diag(A))
    L, U = np.tril(A) - D, np.triu(A) - D
    e = la.norm(b - np.dot(A, x0), 2)
    x, i = x0, 0
    while(tau > e and i <= 100):
        T = -np.dot(la.inv(D), L + U)
        c = np.dot(la.inv(D), b)
        x = np.dot(T, x) + c
        e = la.norm(b - np.dot(A, x), 2)
        print(f"{i + 1}: x = {x.T} - error = {e}")
        i = i + 1
    return x, i

def main():
    A = np.array([[2.,  5.],
                  [1.,  7.]])
    print(f"Matriz A:\n{A}")
    b = np.array([[11.],
                  [13.]])
    print(f"Vector columna b:\n{b}")
    x0 = np.array([[1.],
                   [1.]])
    print(f"Solución x0:\n{x0}")
    iter = 10

    itera = np.arange(1, iter + 1, 1)

    lx, error = Jacobi(A, b, x0, iter)

    for i in range(iter):
        print(f"{i + 1}: x = {lx[i].T} - error = {error[i]}")

    fig, ax = plt.subplots()
    ax.plot(itera, error)

    ax.set(xlabel='iteraciones',ylabel='error',title='Iteraciones vs Error')
    ax.grid()

    plt.show()

if __name__ == "__main__":
    main()