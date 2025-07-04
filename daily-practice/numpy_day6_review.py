import numpy as np

#Create a 2D array and use broadcasting to add a row
a = np.array([[1,2,3],[4,5,6]])
b = np.array([9,6,0])
new_matrix= np.vstack([a , b] )
print(new_matrix)

#Use boolean indexing to filter values > mean
mean = np.mean(new_matrix)
filtered = new_matrix[new_matrix > mean]
print(filtered)

#reshape
new_shape= new_matrix.reshape([9,1])
print("using reshape:\n",new_shape)

#ravel: any changes in it changes the orignal matrix
raveled = np.ravel(new_matrix)
raveled[0]= 69
print(raveled)

#flatten:any changes in it doesn't changes the orignal matrix
flattened = new_matrix.flatten()
flattened[0]= 70
print(flattened)

#difference between flattened and ravel:
print(new_matrix)   # even though [0] index has been changed in bothh in the new_matrix only the change in ravel has been affected


#difference between view and copy
view_array = new_matrix.view()  
copy_array = new_matrix.copy()  
view_array[0, 0] = 99  # Modifies original
copy_array[0, 1] = 88  # Does not affect original
print("View:", view_array)
print("Copy:", copy_array)
print("Original:", new_matrix)

# coditions using where()
filtered_1 = new_matrix[np.where(new_matrix > 2)]
print(filtered_1)

#Use np.argmax() and np.argsort() on a 1D and 2D array

# 1-D:
c = np.array([4,7,12,15,82])
max_index  = np.argmax(c)
sort_index = np.argsort(c)
print(max_index)
print(sort_index)

#2D
max_idx2D = np.argmax(new_matrix)
sort_idx2D = np.argsort(new_matrix)
print(max_idx2D)
print(sort_idx2D)