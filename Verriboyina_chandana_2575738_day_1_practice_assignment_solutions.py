#!/usr/bin/env python
# coding: utf-8

# # LANGUAGE FUNDAMENTALS

# # 1. Manipulate using a list.
# 
#     i)   To add new elements to the end of the list.
# 
#     ii)  To reverse elements in the list.
# 
#     iii) To display the same list of elements multiple times.
# 
#     iv)  To concatenate two list.
# 
#     v)   To sort the elements in the list in ascending order.

# In[1]:


list = [32, 49.99, 'chandana']
list


# In[11]:


# i) To add new elements to the end of the list.

list.append(1000) #append is used to add a single element
list


# In[12]:


list.append('batch-232') #appending one more element into the list
list


# In[34]:


# To add multiple elements at a time, we use 'extend'

list.extend([1,'apple',10.1])
print('Total elements after added are: \n\n', list)


# In[35]:


# ii)  To reverse elements in the list.

list.reverse()
print('The elements after reversed are: \n\n', list)


# In[40]:


# iii) To display the same list of elements multiple times.

repeated_list = list * 3 #Just multiply with the number of times to be repeated 
print('The repeated same list of elements in multiple times are : \n\n', repeated_list)


# In[41]:


# iv) To concatenate two list.

list2 = ['a', 'b']
concatenate_list = list + list2  # '+' operator is used to concatenate the two lists
print('The final list after concatenation is : \n\n', concatenate_list)


# In[46]:


# v) To sort the elements in the list in ascending order.

l1 = [67, 99, 0, 34, 1000, 555]
l1.sort()  # Sorting of integer numbers in ascending order takes place here
l2 = ['Peter', 'John', 'Nick', 'Joseph', 'Antony']
l2.sort()  # Sorting of string names in alphabetical order takes place here

# Sorting of mixed data types of elements does not happen in a list

print('The first sorted list of numbers is : \n\n',l1)
print('\n')
print('The second sorted list of names is : \n\n',l2)


# # 2. Write a Python program to do in the tuples.
# 
# 
#    i)    Manipulate using tuples.
# 
#    ii)   To add new elements to the end of the tuples
# 
#    iii)  To reverse elements in the list
# 
#    iv)   To display the elements of the same tuple multiple times.
# 
#    v)    To concatenate two tuples
# 
#    vi)   To sort the elements in the list in ascending order.

# In[68]:


# i) Manipulate using tuples.

items_tuple = (1, 2, 3)
print(items_tuple)


# In[13]:


# Tuple is converted into list for manipulation purpose

items_tuple = (1, 2, 3)
items_list = list(items_tuple)
print(items_list)


# In[14]:


# ii) To add new elements to the end of the tuples

items_tuple = (1, 2, 3)
items_tuple = items_tuple + (6, 7, 8)
print('After adding new elements : \n\n', items_tuple)


# In[15]:


# iii) To reverse elements in the list

reversed_list = items_tuple[::-1]
print('The reversed list is : \n\n', reversed_list)


# In[1]:


# iv) To display the elements of the same tuple multiple times.

items_tuple = (1, 2, 3)
n = int(input("Enter the value of n: "))
print('Displaying tuple in multiple times : \n\n', items_tuple * n)


# In[2]:


# v) To concatenate two tuples

tuple1 = (88, 77, 66, 55)
tuple2 = (44, 33, 22, 11)
tuple_concat = tuple1 + tuple2
print('The concatenation of two tuples is : \n\n', tuple_concat)


# # vi) To sort the elements in the list in ascending order.
# 
# tuple1 = (88, 77, 66, 55)
# list_tuple1 = list(tuple1)
# print('After sorting the tuple is : \n\n')
# list_tuple1.sort()

# # 3. Write a python program to implement the following using list.
# 
#    i)   Create a list with integers (minimum 10 numbers)
# 
#    ii)  How to display the last number in the list
# 
#    iii) Command for displaying the values from the list [0:4]
# 
#    iv)  Command for displaying the values from the list [2:]
# 
#    v)   Command for displaying the values from the list [:6]

# In[88]:


# i) Create a list with integers (minimum 10 numbers)

list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]
print('The list created was : \n\n', list)


# In[91]:


# ii) How to display the last number in the list

print('The last number present in the list is : ')
list[-1]  # It displays the number present in the index value of '-1' i.e., the last number


# In[93]:


# iii) Command for displaying the values from the list [0:4]

print('The values displayed from the list [0:4] is : ')
list[0:4]  # It displays the values from index[0] to index[4-1] i.e.,index[3]


# In[95]:


# iv) Command for displaying the values from the list [2:]

print('The values displayed from the list [2:] is : ')
list[2:]  # It displays the values from index[2] to till the last index i.e.,index[12]


# In[97]:


# v) Command for displaying the values from the list [:6]

print('The values displayed from the list [:6] is : ')
list[:6]  # It displays the values from first index i.e.,index[0] to index[6-1] i.e.,index[5]


# # 4. Write a Python program: tuple1 = (10,50,20,40,30)
# 
#    i)    To display the elements 10 and 50 from tuple1
# 
#    ii)   To display the length of a tuple1.
# 
#    iii)  To find the minimum element from tuple1.
# 
#    iv)   To add all elements in the tuple1.
# 
#    v)    To display the same tuple1 multiple times.

# In[4]:


# Python program

tuple1 = (10, 50, 20, 40, 30)
print('The tuple created in the python program is : ',tuple1)


# In[106]:


# i) To display the elements 10 and 50 from tuple1.

print("The selected elements from tuple1 are : \n\n", tuple1[0], tuple1[1])


# In[107]:


# ii) To display the length of a tuple1.

print("The length of the tuple1 is : \n\n", len(tuple1))


# In[108]:


# iii) To find the minimum element from tuple1.

print("The minimum element from tuple1 is : \n\n", min(tuple1))


# In[5]:


# iv) To add all elements in the tuple1.

print("The sum of all the elements in tuple1 is : \n\n", sum(tuple1))


# In[6]:


# v) To display the same tuple1 multiple times.

n = int(input("Enter the number of times 'n': "))
print("Displaying the same tuple1 in multiple times is as follows : ", tuple1 * n)


# # 5. Write a Python program:
# 
#   i)   To calculate the length of a string
# 
#   ii)  To reverse words in a string
# 
#   iii) To display the same string multiple times 
# 
#   iv)  To concatenate two strings
# 
#   v)   Str1 = " South India", using string slicing to display "India"

# In[18]:


# i) To calculate the length of a string

String = " Welcome to python "
length = len(String)
print('The length of the String is : ', length)


# In[19]:


# ii) To reverse words in a string

reversed_string = String[::-1]
print('The reversed format of words in a string is : ', reversed_string)


# In[20]:


# iii) To display the same string multiple times

n = int(input("Enter the value of n: "))  # Number of times to display the string
print('Displaying the same string in multiple times: \n', String * n)


# In[22]:


# iv) To concatenate two strings

String_one = "Welcome"
String_two = "Python"
concatenated_string = String_one + ' ' + String_two
print("The concatenated string is : ", concatenated_string)


# In[24]:


# v) Str1 = " South India", using string slicing to display "India"

Str1 = " South India"
Slicing_to_India = Str1[7:]
print("The sliced string to display 'India' here is :", Slicing_to_India)


# # 6. Perform the following: 
# 
#   i)    Creating the Dictionary.
# 
#   ii)   Accessing values and keys in the Dictionary.
# 
#   iii)  Updating the dictionary using a function.
# 
#   iv)   Clear and delete the dictionary values.

# In[38]:


# i) Creating the Dictionary

dictionary = {'First_name': 'Verriboyina', 'Last_name': 'Chandana', 'Age': 22}
print('The dictionary created was :', dictionary) 


# In[33]:


# ii) Accessing values and keys in the Dictionary.

fname = dictionary['First_name']
lname = dictionary['Last_name']
age = dictionary['Age']
print('Accessing values and keys in the Dictionary :', '\nFirst_name : ', fname, '\nLast_name : ', lname, '\nAge : ', age)


# In[39]:


# iii) Updating the dictionary using a function.

def updating_age(dictionary, new_age):
    dictionary['Age'] = new_age
    print('\nAfter updation : ', dictionary)

print('Now, we are updating the age\n\n Before updation : ', dictionary)
updating_age(dictionary, 25)


# In[40]:


# iv) Clear and delete the dictionary values.

dictionary.clear()  # Clearing all the items in dictionary
print("The cleared Dictionary is : ", dictionary)

del dictionary  # Deleting the entire dictionary
 
dictionary  # Attempting to access dictionary will give an error here because it is already deleted.


# # 7. Python program to insert a number to any position in a list.

# In[49]:


list = [0, 1, 2, 4, 5]  # Creating a list
print("The intial list is : ", list)
inserting_num = 3   # The number to  be inserted
position = 3  # Position where the number should be inserted
length = len(list)  # Finding the length of the list
# Checking if the position is within the given index range of the list or not
if (position >= 0) and (position <= length):
    list.insert(position, inserting_num)
    print("\nThe updated list is : ", list)
else:
    print("\nPosition value should be between 0 and ", length)


# # 8. Python program to delete an element from a list by index. 

# In[51]:


list = [1, 2, 3, 4, 5, 6]  # Creating a list
print("The intial list is : ", list)
deleting_num = 3   # The number to be deleted
position = 2  # Position where the number should be deleted
length = len(list)  # Finding the length of the list
# Checking if the position is within the given index range of the list or not
if (position >= 0) and (position <= length):
    del list[position]
    print("\nThe updated list after deletion is : ", list)
else:
    print("\nPosition value should be between 0 and ", length)


# # 9. Write a program to display a number from 1 to 100.

# In[58]:


number = int(input("Enter the number : "))
if (number>=1) and (number<=100):
    print('The given number', number, 'is from 1 to 100')
else:
    print('The given number is not from 1 to 100')


# # 10. Write a Python program to find the sum of all items in a tuple.

# In[59]:


tuple = (10, 20, 30, 40)
print('The sum of all items in the tuple is : ', sum(tuple))


# # 11. Create a dictionary containing three lambda functions square, cube and square root.
# 
#    i)   E.g. dict = {'Square': function for squaring, 'Cube': function for cube, 'Squareroot':
# 
#         function for square root}
# 
#    ii)  Pass the values (input from the user) to the functions in the dictionary respectively.
# 
#    iii) Then add the outputs of each function and print it.

# # 12. A list of words is given. Find the words from the list that have their second character in uppercase.
# 
#     ls = ['hello', 'Dear', 'hOw', 'ARe', 'You']

# In[67]:


ls = ['hello', 'Dear', 'hOw', 'ARe', 'You']
words = []

for i in ls:
    if i[1].isupper():
        words.append(i)

print("The words from the list that have their second character in uppercase are :", words)


# # 13. A dictionary of names and their weights on earth is given. Find how much they will weigh on the moon. (Use map and lambda functions) Formula: wMoon = (wEarth * GMoon) / GEarth
# 
#        i)     #Weight of people in kg
# 
#                    WeightOnEarth = {'John':45, 'Shelly':65, 'Marry':35}
#             
#        ii)    #Gravitational force on the Moon: 1.622 m/s2
# 
#                    GMoon = 1.622
# 
#        iii)   #Gravitational force on the Earth: 9.81 m/s2
# 
#                    GEarth = 9.81

# In[ ]:




