A = np.double(plt.imread('mm.gif'))
print(np.shape(A))
print(np.linalg.matrix_rank(A))
for k in range(-3,1):
    print(np.linalg.matrix_rank(A,tol=10**k))