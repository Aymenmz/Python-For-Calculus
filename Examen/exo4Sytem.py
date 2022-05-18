import numpy as np
from numpy import linalg as al
A = np.array(
    [[1, 2, 5],
     [2, 3, 9],
     [5, 1, 8]],
    dtype=float
)

B = np.array([1, 3, 2])
Ainv = al.inv(A)
print(Ainv)

res = al.solve(A, B)
print("Le resultat est : "+str(res))

