def gaussian_elimination(A,verbose=True):
    m, n = np.shape(A)
    piv = np.zeros(m).astype(int)
    i, j = 0, 0
    while i < m and j < n:
        k = i
        while k < m and abs(A[k,j]) < 10**(-6):
            k += 1
        if k == m:
            j += 1
        else:
            if k > i:
                A[[k,i]] = A[[i,k]]
                if verbose:
                    print(f"Swapped row {i} and {k}:\n", A)
            A[i,j:] = A[i,j:]/A[i,j]
            if verbose:
                print(f"created a leading one at pos. ({i},{j}):\n",A)
            A[(i+1):,j:] = A[(i+1):,j:] - A[(i+1):,[j]] @ A[[i],j:]
            if verbose:
                print(f"zeroed out below row {i} in col. {j}:\n", A)
            piv[i] = j
            i += 1; j += 1
    i -= 1
    while i > 0:
        j = piv[i]
        A[:i,j:] = A[:i,j:] - A[:i,[j]] @ A[[i], j:]
        if verbose:
            print(f"zeroed out above row {i} in col. {j}:\n", A)
        i -= 1