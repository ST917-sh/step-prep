import numpy as np

# 1. Create an array of 10 random integers between 1 and 100
a = np.random.randint(1,101,10)
print('Array A:',a)

# 2. Print only the even numbers from the array using boolean masking
a_even = a[a%2 == 0] 
print('Even numbers:', a_even)

# 3. Print the indices of all values greater than 50
indices = np.where(a > 50)
print('no. grater than 50', indices)

#4. Replace all odd numbers in 'a' with -1
a[a% 2 !=0]= -1
print(a)