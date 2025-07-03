import numpy as np

# 1. Create a 2D array (3x3) filled with 10s
a = np.full((3,3) , 10)
print(a)

# 2. Create a 1D array: [1, 2, 3]
b = np.array([1,2,3])
print(b)

# 3. Add the 1D array to each row of the 2D array
result = b + a
print(result)

# 4. Subtract the 1D array from each column of the 2D array
result_4 = (a.T-b).T
print(result_4)

# 5. Multiply a 1D array of shape (3,) with a column vector of shape (3,1)
col_vector = np.array([[1],[2],[3]])
row_vector= np.array([5,6,7])
vector_mul = col_vector*row_vector
print(vector_mul)