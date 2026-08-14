def mult_PkT_left(A, r, s, theta):
    a = np.cos(theta)*A[[r-1],:] - np.sin(theta)*A[[s-1],:]
    b = np.sin(theta)*A[[r-1],:] + np.cos(theta)*A[[s-1],:]
    A[[r-1,s-1],:] = np.block([[a],[b]])

def mult_Pk_right(A, r, s, theta):
    a = np.cos(theta)*A[:,[r-1]] - np.sin(theta)*A[:,[s-1]]
    b = np.sin(theta)*A[:,[r-1]] + np.cos(theta)*A[:,[s-1]]
    A[:,[r-1,s-1]] = np.block([[a,b]])

def eig_jacobi_2(A):
    A = A.copy()
    tol=10**(-4)
    n = np.shape(A)[0]
    P = np.eye(n)
    while off(A) > tol:
        r, s = offabsmaks(A)
        theta = np.arctan( 2*A[r-1,s-1]/(A[s-1,s-1]-A[r-1,r-1]) )/2
        mult_Pk_right(A, r, s, theta)
        mult_PkT_left(A, r, s, theta)
        mult_Pk_right(P, r, s, theta)
    return A, P