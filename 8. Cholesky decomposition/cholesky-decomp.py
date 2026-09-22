import numpy as np
from math import sqrt

#Test Matrix construction
#We create a lower triangular 5x5 matrix 'A' with non-zero diagonal entries (it has a full rank)
A = np.array( [ [1,0,0,0,0],
                [1,2,0,0,0], 
                [1,2,3,0,0], 
                [1,2,3,4,0], 
                [1,2,3,4,5] ], dtype='float' )

#We define the symmetric matrix S = A^T * A (S is obtained by multiplying the transpose of matrix A by A)
#Due to this construction and the full rank of matrix A, S is symmetric and positive definite by definition 
S = np.dot( A.T, A )

#Cholesky decomposition function
def cholesky(a):
    #We create a copy matrix, 'temp', of the original matrix 'A' to perform in-place calculations
    temp = a.copy()
    #The size of the matrix
    n = a.shape[0]
   #Implementation adapted to Python's 0-based indexing:
    for j in range (n):
        #We update the entries of column j by subtracting the contribution of previous columns k:
        for k in range (j):
            for i in range(j,n):
                temp[i, j] -= temp[i, k] * temp[j, k] 

        #We compute the diagonal element: temp[j, j] = sqrt(temp[j, j])
        temp[j,j] = sqrt(temp[j,j])
        #We scale the subdiagonal entries of the current column by dividing them by temp[j, j]
        for k in range(j+1, n):
            temp[k,j] = temp[k,j]/temp[j,j]
    #We only return the lower triangular part of the 'temp matrix, zeroing out the remaining elements of the upper triangle
    return np.tril(temp)

#We compute the lower triangular matrix L, for matrix S
L = cholesky(S)

#We print the original matrix A
print('A')
print(A)

#We print the symmetric matrix S obtained by multiplying transpose of A by A (S = A^T * A)
print('S')
print(S)

#We print the lower triangular matrix L obtained from the Cholesky decomposition function
print('L')
print(L)

#VERIFICATION CHECK
#We compute the product L * L^T using np.dot(L, L.T), which should numerically match the original matrix S
print('check')
print(np.dot(L, L.T))