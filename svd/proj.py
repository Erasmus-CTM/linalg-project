def proj(x,m_min_k):
    y = np.zeros(np.shape(x))
    m = int(np.log2(len(x))); k = m - m_min_k
    for r in range(0,2**m,2**(m-k)):
        y[r:(r+2**(m-k)),:]=np.sum(x[r:(r+2**(m-k)),:],0)
    return y/2**(m-k)