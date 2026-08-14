def qr_impl(A,n):
    Q, R = np.linalg.qr(A)
    for k in range(n):
        A = R @ Q
        Q, R = np.linalg.qr(A)
        print(A)