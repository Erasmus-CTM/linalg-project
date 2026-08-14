def power_impl(A,k):
    n = np.shape(A)[0]
    x = np.ones((n,1))
    for r in range(k):
        x = A @ x
        mu = np.max(abs(x))
        x = (1/mu)*x
    return mu, x