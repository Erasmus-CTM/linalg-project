def compute_fourier(t, c):
    N = (len(c)-1)/2
    n = np.arange(-N,N+1).reshape((1,-1)).astype(float)
    return np.exp(2*np.pi*1j*n*t/T) @ c