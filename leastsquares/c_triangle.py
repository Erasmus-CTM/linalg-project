def c_triangle(N):
    n = np.arange(-N,N+1).reshape((1,-1)).astype(float)
    n = np.delete(n, N, axis=1)
    I_00 = (T/(2*np.pi*1j*n))*(1-(-1)**n)
    I_01 = -I_00
    I_10 = -(T**2/(4*np.pi*1j*n))*(-1)**n \
           +(T/(2*np.pi*1j*n))*I_00
    I_11 = (-1)**n * ( (T/2)*I_00 + I_10  )
    I_0 = I_00 - (4/T)*I_10 
    I_1 = (4/T)*I_11 - 3*I_01
    c = (I_0+I_1).T/T
    c = np.insert(c, N, 0, axis=0)
    return c