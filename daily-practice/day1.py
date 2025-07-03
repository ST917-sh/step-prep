import numpy as np

#1. Create a 1D NumPy array with numbers from 10 to 50 (inclusive) with a step of 10
A = np.arange(10,60,10)
print(A)

#2. Create a 2D array with shape (2, 3) filled with all 5s
B = np.full((2,3),5)
print(B)

# 3. Add the 1D array to itself (element-wise)
A_sum = A + A
print(A_sum)

# 4. Multiply the 2D array by 3
B_new = B * 3
print(B_new)