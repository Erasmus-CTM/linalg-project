def mult_PkT_left(A, r, s, theta):
    a = np.cos(theta)*A[[r-1],:] - np.sin(theta)*A[[s-1],:]
    b = np.sin(theta)*A[[r-1],:] + np.cos(theta)*A[[s-1],:]
    A[[r-1,s-1],:] = np.block([[a],[b]])