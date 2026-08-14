def eig_jacobi(A):
    tol=10**(-4)
    n = np.shape(A)[0]
    P = np.eye(n)
    while off(A) > tol:
        r, s = offabsmaks(A)
        theta = np.arctan( 2*A[r-1,s-1]/(A[s-1,s-1]-A[r-1,r-1]) )/2
        Pk = P_k(r, s, theta, n)
        A = Pk.T @ A @ Pk
        P = P @ Pk
    return A, P