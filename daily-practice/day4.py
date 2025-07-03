import numpy as np

# 1. Create a 3x3 array with values from 1 to 9
a = np.arange(1,10).reshape(3,3)
print(a)

# 2. Slice and print the first two rows
print(a[:2])

# 3. Slice and print the last two columns
print(a[1:])

# 4. Print the element at row 2, column 3 (zero-indexed)
print(a[1,2])

# 5. Flatten the array
b = a.flatten()
print(b)
