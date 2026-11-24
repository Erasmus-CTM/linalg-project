def c_sampling(N, func):
    M=2*N+1
    tsp = np.linspace(0,T-T/M,M).reshape((-1,1))
    fsp = func(tsp)
    n = np.arange(-N,N+1).reshape((1,-1))
    A = np.exp(2*np.pi*1j*n*tsp/T)
    return np.linalg.solve(A, fsp)