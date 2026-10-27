def eig_qr(A):
    tol=10**(-4)
    n = np.shape(A)[0]
    P = np.eye(n)
    while off(A) > tol:
        Q, R = np.linalg.qr(A)
        A = R @ Q
        P = P @ Q
    return A, P