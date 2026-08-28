def simpsonn(f, a, b, n):
    h = (b - a)/(2*n)
    return h*( f(a) + f(b) + 2*sum( f(a+2*h*np.arange(1,n) ))  \
                    + 4*sum( f(a+h+2*h*np.arange(0,n))))/3