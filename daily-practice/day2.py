import numpy as np

# Task 1: Create a 2D array of shape (3, 4) filled with random integers between 10 and 50
a = np.random.randint(10, 51, size=(3, 4))
print("Array a:\n", a)

# Task 2: Print the mean, median, standard deviation, and sum of all values
print("Mean:", np.mean(a))             # Average of all numbers
print("Median:", np.median(a))         # Middle number when sorted
print("Standard Deviation:", np.std(a))# Spread of numbers (how far from mean)
print("Sum:", np.sum(a))               # Total sum

# Task 3: Flatten the array and print the first 5 elements
flattened = a.flatten()                # Converts 2D to 1D
print("First 5 elements:", flattened[:5])

