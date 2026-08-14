def P_k(r,s,theta,n):
    P = np.eye(n)
    P[r-1,r-1] = np.cos(theta); P[r-1,s-1] = np.sin(theta)
    P[s-1,r-1] = -np.sin(theta); P[s-1,s-1] = np.cos(theta)
    return P