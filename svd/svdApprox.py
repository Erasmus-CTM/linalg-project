def svdApprox(A,k):
    m,n = np.shape(A)
    assert k <= np.min([m,n]), 'we must have k<= min(m,n)!'
    U,S,V = np.linalg.svd(A)
    AK = np.zeros((m,n))
    for i in range(k):
        AK = AK + S[i]*U[:,[i]]@V[[i],:]
    return AK