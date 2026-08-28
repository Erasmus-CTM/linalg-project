def trapezoidaln(f, a, b, n):
    h = (b - a)/n
    return h*( (f(a) + f(b))/2 + sum( f(a + np.arange(1,n)*h)))