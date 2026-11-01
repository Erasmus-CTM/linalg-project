def P_from_phi_m(y):
    x = np.zeros(np.shape(y))
    N=np.shape(y)[0]; Nhalf = int(N/2)
    x[0:Nhalf,:] = y[0::2,:] + y[1::2,:]
    x[Nhalf:,:] = -y[0::2,:] + y[1::2,:]
    x = x/2
    return x