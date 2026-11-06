m=6
x = np.linspace(-1+1/m,1-1/m,m)
k = np. arange(1,m+1).reshape((-1,1))
l = np.arange(1,m+1).reshape((1,-1))

G = np.zeros((m,m))
for xval in x:
    G += xval**(k+l-2)
G = G/m