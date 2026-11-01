def P_to_phi_m(x):
    y = np.zeros(np.shape(x))
    N=np.shape(x)[0]; Nhalf = int(N/2)
    y[0::2,:] = x[:Nhalf,:] -  x[Nhalf:,:]
    y[1::2,:] = x[:Nhalf,:] + x[Nhalf:,:]
    return y