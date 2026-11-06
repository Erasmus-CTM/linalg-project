R = np.eye(m); A = np.eye(m)
Q = np.zeros((m,m)); Q[:,0] = A[:,0];
for j in range(1,m):
    R[[j-1],j:] = (Q[:,[j-1]].T @ G @ A[:,j:])/(Q[:,[j-1]].T @ G @ Q[:,[j-1]])
    Q[:,[j]] = A[:,[j]] - Q[:,:j]@R[:j,[j]]

for j in range(m):
    nrm = np. sqrt( Q[:,[j]].T @ G @ Q[:,[j]] )
    Q[:,[j]] = Q[:,[j]]/nrm
    R[[j],:] = nrm*R[[j],:]