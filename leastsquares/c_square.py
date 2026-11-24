def c_square(N):
    n = np.arange(-N,N+1).reshape((1,-1)).astype(float)
    n = np.delete(n, N, axis=1)
    c = ((1-(-1)**n)/(np.pi*1j*n)).T
    c = np.insert(c, N, 0, axis=0)
    return c