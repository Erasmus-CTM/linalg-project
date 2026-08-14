def off(A):
    all = np.sum(np.sum(A**2))
    diag = np.sum(np.diag(A)**2)
    return np.sqrt( all - diag )