def C(A):
    n=np.shape(A)[0]
    pol=np.poly(A)
    pol=np.flip(pol)      # Reverse the order, since the highest coefficients are first
    C = np.zeros((n,n))
    C[:(n-1),1:] = np.eye(n-1)
    C[n-1,:] = -pol[:n]
    return C