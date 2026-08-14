def relError(A,AK):
    normF = np.sqrt( np.sum((A-AK)**2) )
    normA = np.sqrt( np.sum(A**2) )
    return normF/normA