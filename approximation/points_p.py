def points_p(find_c, N):
    n = np.arange(-N,N+1).reshape((1,-1))
    c = find_c(N)
    return np.real( np.exp(2*np.pi*1j*n*tp/T) @ c )