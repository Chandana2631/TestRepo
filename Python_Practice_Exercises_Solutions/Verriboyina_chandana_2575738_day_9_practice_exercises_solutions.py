#!/usr/bin/env python
# coding: utf-8

# # NUMPY PROBLEMS

# # 1. Create a 3x3x3 array with random values.

# In[7]:


import numpy as np

array = np.random.rand(3, 3, 3)
print('The (3x3x3) array with random values is as follows :\n')
print(array)


# # 2. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal.

# In[9]:


import numpy as np

# Creating a 5x5 matrix filled with zeros
matrix = np.zeros((5, 5))

# Set values 1, 2, 3, and 4 just below the diagonal
for i in range(1, 5):
    matrix[i, i-1] = i
print('The (5x5) matrix with values 1,2,3,4 just below the diagonal is :\n')
print(matrix)


# # 3. Create a 8x8 matrix and fill it with a checkerboard pattern.

# In[12]:


import numpy as np

# Creating an 8x8 matrix filled with zeros
matrix = np.zeros((8, 8), dtype=int)

# Filling the checkerboard pattern with alternating 1s and 0s
matrix[1::2, ::2] = 1
matrix[::2, 1::2] = 1
print('The (8x8) matrix filled with a checkerboard pattern is :\n')
print(matrix)


# # 4. Normalize a 5x5 random matrix.

# In[17]:


import numpy as np

# Creating a random 5x5 matrix
random_matrix = np.random.rand(5, 5)

# Calculating the minimum and maximum values in the matrix
min_value = np.min(random_matrix)
max_value = np.max(random_matrix)

# Normalizing the matrix between 0 and 1
normalized_matrix = (random_matrix - min_value) / (max_value - min_value)

print('The Random Matrix is :\n')
print(random_matrix)
print('\nThe Normalized Matrix is :\n')
print(normalized_matrix)


# # 5. How to find common values between two arrays?

# In[18]:


import numpy as np

arr1 = np.array([2, 4, 6, 8])
arr2 = np.array([2, 3, 4, 5])

# Finding common values between the two arrays
common_values = np.intersect1d(arr1, arr2)
print('The common values between two arrays is :', common_values)


# # 6. How to get the dates of yesterday, today and tomorrow?

# In[23]:


import numpy as np
from datetime import datetime, timedelta

# Get today's date
today = datetime.now().date()

# Calculating yesterday and tomorrow
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)

# Formatting the dates as strings is optional
today_str = today.strftime('%Y-%m-%d')
yesterday_str = yesterday.strftime('%Y-%m-%d')
tomorrow_str = tomorrow.strftime('%Y-%m-%d')

# Creating a NumPy array with yesterday, today, and tomorrow
arr = np.array([yesterday_str, today_str, tomorrow_str])

print('Yesterday :', arr[0])
print('Today :', arr[1])
print('Tomorrow :', arr[2])


# # 7. Consider two random array A and B, check if they are equal.

# In[26]:


import numpy as np

# Creating two random arrays A and B
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
print('Array A is :\n', A)
print('\nArray B is :\n', B)

# Checking if A and B are equal or not
are_equal = np.all(A == B)

if are_equal:
    print('\nA and B are equal.')
else:
    print('\nA and B are not equal.')


# # 8. Create random vector of size 10 and replace the maximum value by 0.

# In[28]:


import numpy as np

vector = np.random.rand(10)
print('The random vector is :\n', vector)

max_index = np.argmax(vector)
vector[max_index] = 0

print('\nThe random vector of size 10 after replace the maximum value by 0 is :')
print(vector)


# # 9. How to print all the values of an array?

# In[34]:


import numpy as np

arr = np.array([11, 22, 33, 44, 55, 66])
print('The array is :', arr)
print('\nThe values in the array are as follows :')
for i in arr:
    print(i)


# # 10. Subtract the mean of each row of a matrix.

# In[83]:


import numpy as np

matrix = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])

# Calculating the mean of each row
row_mean = np.mean(matrix, axis = 1)

# Subtracting the row mean from the matrix
new_matrix = matrix - row_mean[:, np.newaxis]

print(' The Original Matrix is :\n', matrix)
print('\nThe mean of each row is :', row_mean)
print('\nThe new matrix after subtracting the mean of each row of a matrix is :\n', new_matrix)


# # 11. Consider a given vector, how to add 1 to each element indexed by a second vector (be careful with repeated indices)?

# In[82]:


import numpy as np

# Given vector
vector = np.array([44, 55, 66, 77, 88])
print('The given vector is :', vector)

# Indices where 1 is added
indices = np.array([1, 3, 0])

# Adding 1 to each element in the indices array
vector[indices] += 1
print('\nAfter adding 1 to each element in the indices array,\nThe second vector is :', vector)


# # 12. How to get the diagonal of a dot product?

# In[41]:


import numpy as np

matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print('The first matrix is :\n', matrix1)
matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])
print('\nThe second matrix is :\n', matrix2)

dot_product = np.dot(matrix1, matrix2)
diagonal = np.diag(dot_product)

print('\nThe Dot Product is :\n', dot_product)
print('\nThe Diagonal of Dot Product is :\n', diagonal)


# # 13. How to find the most frequent value in an array?

# In[52]:


import numpy as np

arr = np.random.randint(0,10,50)
print('The random array is :\n', arr)
most_frequent = np.argmax(np.bincount(arr))
print('\nThe Most frequent value in the array is :', most_frequent)


# # 14. How to get the n largest values of an array?

# In[56]:


import numpy as np

arr = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
n = 3
print('The array is :', arr)
largest_values = np.partition(arr, -n)[-n:]
print('\nThe first {} largest values in the array are : {}'.format(n,largest_values))


# # 15. How to create a record array from a regular array?

# In[15]:


import numpy as np

# Creating a regular array
regular_array = np.array([(1, 'Apple', 'red'),(2, 'Banana', 'yellow'),(3, 'Cherry', 'red')], dtype=[('id', int), ('name', 'U10'), ('color', 'U10')])
print('The Regular array is :', regular_array)

# Converting the regular array to a record array
record_array = np.rec.array(regular_array)
print('\nThe Record array is :', record_array)
print("\nThe columns are :\nID:", record_array['id'])
print("Name:", record_array['name'])
print("Age:", record_array['color'])


# # 16. How to swap two rows of an array?

# In[67]:


import numpy as np

array = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print('The array is :\n', array)
# Define the indices of the rows you want to swap
row1_index = 0 
row2_index = 2 

# Swap the rows
array[row1_index], array[row2_index] = array[row2_index].copy(), array[row1_index].copy()
print('\nThe array after swapping the rows {} and {} is : \n{}'.format(row1_index + 1, row2_index + 1, array))


# # 17. Write python code to reshape to the next dimension of numpy array?

# In[18]:


import numpy as np

# 1D array
arr = np.array([[20, 30, 40, 50, 60, 70]])

# Calculate the size of the new shape (2D in this case)
new_shape = (-1, 2)  # -1 means the size will be automatically calculated

# Reshape the array to the new shape
reshaped_arr = arr.reshape(new_shape)

print('The Original 1D Array is :\n', arr)
print('\nThe Reshaped 2D Array is :\n', reshaped_arr)

