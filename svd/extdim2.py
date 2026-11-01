def extdim2(A,P):
    B=P(A).transpose()
    return P(B).transpose()