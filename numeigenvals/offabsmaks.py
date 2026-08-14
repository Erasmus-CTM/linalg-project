def offabsmaks(A):
    B = abs(A)
    n = np.shape(A)[0]
    for k in range(n):
        B[k,k] = 0
    maxvals = np.max(B, axis=0)
    s = np.argmax(maxvals)
    r = np.argmax(B[:, s])
    return r + 1, s + 1