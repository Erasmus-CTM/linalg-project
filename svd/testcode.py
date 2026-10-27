import matplotlib.pyplot as plt
import numpy as np

A=plt.imread('mm.gif')
print(A)
print(np.shape(A))

def row(m, A, f):
    f.write('[')
    for n in range(255):
        f.write(str(A[m,n]))
        f.write(',')
    f.write(str(A[m,255]))
    f.write(']')
    
f = open('mmasarray.py','w')
f.write('A=np.array([')
for m in range(255): 
    row(m, A, f)
    f.write(',')
row(255, A, f)
f.write("], dtype='d')")
f.close()