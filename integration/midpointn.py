def midpointn(f, a, b, n):
    h = (b - a)/n
    return h*sum( f(a + h/2 + np.arange(0,n)*h))