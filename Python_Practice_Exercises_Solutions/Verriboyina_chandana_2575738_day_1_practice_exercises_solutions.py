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

# In[11]:


list = [32, 49.99, 'chandana']
print('List =', list)


# In[12]:


# i) To add new elements to the end of the list.

list.append(1000) #append is used to add a single element
print('List =', list)


# In[13]:


list.append('batch-232') #appending one more element into the list
print('List =', list)


# In[14]:


# To add multiple elements at a time, we use 'extend'

list.extend([1,'apple',10.1])
print('Total elements after added are: \n\nList =', list)


# In[15]:


# ii)  To reverse elements in the list.

list.reverse()
print('The elements after reversed are: \n\nList =', list)


# In[16]:


# iii) To display the same list of elements multiple times.

repeated_list = list * 3 #Just multiply with the number of times to be repeated 
print('The repeated same list of elements in multiple times are : \n\nList =', repeated_list)


# In[17]:


# iv) To concatenate two list.

list2 = ['a', 'b']
concatenate_list = list + list2  # '+' operator is used to concatenate the two lists
print('The final list after concatenation is : \n\nList =', concatenate_list)


# In[18]:


# v) To sort the elements in the list in ascending order.

l1 = [67, 99, 0, 34, 1000, 555]
l1.sort()  # Sorting of integer numbers in ascending order takes place here
l2 = ['Peter', 'John', 'Nick', 'Joseph', 'Antony']
l2.sort()  # Sorting of string names in alphabetical order takes place here

# Sorting of mixed data types of elements does not happen in a list

print('The first sorted list of numbers is : \n\nList1 =',l1)
print('\n')
print('The second sorted list of names is : \n\nList2 =',l2)


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

# In[5]:


# i) Manipulate using tuples.

items_tuple = (1, 2, 3)
print('Tuple is',items_tuple)
print('\nThe type of items_tuple is')
type(items_tuple)


# In[6]:


# Tuple is converted into list for manipulation purpose

items_tuple = (1, 2, 3)
items_list = list(items_tuple)
print(items_list)
print('\nType of items_list is')
type(items_list)


# In[7]:


# ii) To add new elements to the end of the tuples

items_tuple = (1, 2, 3)
items_tuple = items_tuple + (6, 7, 8)
print('After adding new elements : \n\nTuple =', items_tuple)


# In[8]:


# iii) To reverse elements in the list

reversed_list = items_tuple[::-1]
print('The reversed list is : \n\nTuple =', reversed_list)


# In[9]:


# iv) To display the elements of the same tuple multiple times.

items_tuple = (1, 2, 3)
n = int(input("Enter the value of n: "))
print('Displaying tuple in multiple times : \n\nTuple =', items_tuple * n)


# In[10]:


# v) To concatenate two tuples

tuple1 = (88, 77, 66, 55)
tuple2 = (44, 33, 22, 11)
tuple_concat = tuple1 + tuple2
print('The concatenation of two tuples is : \n\nTuple =', tuple_concat)


# In[18]:


# vi) To sort the elements in the list in ascending order.

tuple1 = (88, 77, 66, 55)
list_tuple1 = list(tuple1)
print('After sorting the tuple is : \n')
list_tuple1.sort()
print(list_tuple1)


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

# In[39]:


# i) Creating the Dictionary

dictionary = {'First_name': 'Verriboyina', 'Last_name': 'Chandana', 'Age': 22}
print('The dictionary created was :', dictionary) 


# In[40]:


# ii) Accessing values and keys in the Dictionary.

fname = dictionary['First_name']
lname = dictionary['Last_name']
age = dictionary['Age']
print('Accessing values and keys in the Dictionary :', '\nFirst_name : ', fname, '\nLast_name : ', lname, '\nAge : ', age)


# In[41]:


# iii) Updating the dictionary using a function.

def updating_age(dictionary, new_age):
    dictionary['Age'] = new_age
    print('\nAfter updation : ', dictionary)

print('Now, we are updating the age\n\n Before updation : ', dictionary)
updating_age(dictionary, 25)


# In[42]:


# iv) Clear and delete the dictionary values.

dictionary.clear()  # Clearing all the items in dictionary
print("The cleared Dictionary is : ", dictionary)

del dictionary  # Deleting the entire dictionary
 
# dictionary  # Attempting to access dictionary will give an error here because it is already deleted.


# # 7. Python program to insert a number to any position in a list.

# In[43]:


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

# In[44]:


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

# In[45]:


number = int(input("Enter the number : "))
if (number>=1) and (number<=100):
    print('The given number', number, 'is from 1 to 100')
else:
    print('The given number is not from 1 to 100')


# # 10. Write a Python program to find the sum of all items in a tuple.

# In[46]:


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

# In[47]:


# Defining a dictionary with lambda functions
dict = {'Square': lambda x: x ** 2, 'Cube': lambda x: x ** 3, 'Square Root': lambda x: x ** 0.5}

#Giving input from the user
user_input = int(input("Enter the number : "))

# Initializing a variable to add the outputs of each function
output_sum = 0

# Applying functions and adding their outputs
for key, function in dict.items():
    output = function(user_input)
    print(key,' of', user_input, ' is', output)
    output_sum = output_sum + output
    
# Printing the sum of all functional outputs
print('Sum of all function outputs is: ', output_sum)


# # 12. A list of words is given. Find the words from the list that have their second character in uppercase.
# 
#     ls = ['hello', 'Dear', 'hOw', 'ARe', 'You']

# In[49]:


ls = ['hello', 'Dear', 'hOw', 'ARe', 'You']
words = []

for i in ls:
    if i[1].isupper():
        words.append(i)

print("\nThe words from the list that have their second character in uppercase are :", words)


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

# In[15]:


#Weight of people in kg
WeightOnEarth = {'John':45, 'Shelly':65, 'Marry':35}

#Gravitational force on the Moon: 1.622 m/s2
GMoon = 1.622

#Gravitational force on the Earth: 9.81 m/s2
GEarth = 9.81

# Use map and lambda to calculate weight on the moon for each person
Weight_On_Moon = list(map(lambda name, weight: (weight * GMoon) / GEarth, WeightOnEarth.keys(), WeightOnEarth.values()))

# Create a dictionary with names and weights on the Moon
Weight_On_Moon = dict(zip(WeightOnEarth.keys(), Weight_On_Moon))

print('The weight on the Moon:\n')
for name, weight in Weight_On_Moon.items():
    print('{}: {} kg'.format(name, weight))


# # CONTROL STRUCTURES:

# # 1. Write a python program to find the first N Prime numbers.

# In[53]:


n = int(input('Enter the value of n : '))
print('\nThe first {} prime numbers are : \n'.format(n))
count = 1  #  Intializing the count value to one
range_num = 2  #  Intializing the end range in for loop as two
while (count<=n):  #  Checks the condition until the required prime numbers are obtained
    prime = True  #  Let the number be assigned as prime intially
    for i in range(2, range_num):  #  checking from 2 to the end range using for loop
        if (range_num % i) == 0:  #  Dividing the number with the integers that range within the number only
            prime = False  #  If remainder is '0', then the number divides with the integer, so it is not a prime
            break  
    if (prime):   #  if it is a prime number then prints it
        print(range_num)
        count = count + 1 
    range_num = range_num + 1  # increasing the range value until it satisfies the count condition


# # 2. Write the python code that calculates the salary of an employee. Prompt the user to enter the Basic Salary, HRA, TA, and DA. Add these components to calculate the Gross Salary. Also, deduct 10% of salary from the Gross Salary to be paid as tax and display gross minus tax as net salary.

# In[54]:


Basic_Salary = float(input('Enter the Basic Salary : '))
HRA = float(input('Enter the HRA : '))
TA = float(input('Enter the TA : '))
DA = float(input('Enter the DA : '))  

Gross_Salary = Basic_Salary + HRA + TA + DA  # Adding all to get the Gross Salary
Tax = (10/100) * Gross_Salary  # Calculating the tax as given condition
net_salary = Gross_Salary - Tax  # Calculating the net salary as given condition

print('Gross Salary is :', Gross_Salary)
print('Tax deduction of 10 % is :', Tax)
print('The overall Net Salary is :', net_salary)


# # 3. Write a python program to search for a string in the given list.

# In[55]:


list = ['Red', 'Blue', 'Green', 'Yellow', 'Black']
String = input('Enter a string to search for in the given list : ')
count = 0
for color in list:
    if String == color:
        count = 1
        print('\nThe color {} was found in the given list'.format(String))
        break
if (count!=1):     
    print('\nThe color {} was not found in the given list'.format(String))    
        


# # 4. Write a Python function that accepts a string and calculates the number of upper-case letters and lower-case letters.

# In[56]:


String = input("Enter the string : ")
upper_case_count = 0
lower_case_count = 0

for letter in String:
    if letter.isupper():
        upper_case_count = upper_case_count + 1
    elif letter.islower():
        lower_case_count = lower_case_count + 1
        
print('\nThe no.of upper-case letters are :', upper_case_count)
print('\nThe no.of lower-case letters are :', lower_case_count)


# # 5. Write a program to display the sum of odd numbers and even numbers that fall between 12 and 37.

# In[58]:


print('Displaying the sum of odd numbers and sum of even numbers that fall between 12 and 37')

odd_sum = 0
even_sum = 0

for i in range(12, 38):
    if (i % 2) != 0:
        odd_sum = odd_sum + i
    else:
        even_sum = even_sum + i

print('\nSum of odd numbers is :', odd_sum)
print('\nSum of even numbers is :', even_sum)


# # 6. Write a python Program to print the table of any number.

# In[59]:


number = int(input('Enter any number : '))
print('The multiplication table of {} is : \n'.format(number))

for i in range(1, 11):
    product = i * number
    print('{} x {} = {}'.format(number,i,product))


# # 7. Write a Python program to sum the first 10 prime numbers.

# In[60]:


n = 10
print('\nThe sum of first {} prime numbers is : \n'.format(n))
count = 1  #  Intializing the count value to one
range_num = 2  #  Intializing the end range in for loop as two
sum = 0

while (count<=n):  #  Checks the condition until the required prime numbers are obtained
    prime = True  #  Let the number be assigned as prime intially
    for i in range(2, range_num):  #  checking from 2 to the end range using for loop
        if (range_num % i) == 0:  #  Dividing the number with the integers that range within the number only
            prime = False  #  If remainder is '0', then the number divides with the integer, so it is not a prime
            break  
    if (prime):   #  if it is a prime number then prints it
        sum = sum + range_num
        count = count + 1 
    range_num = range_num + 1  # increasing the range value until it satisfies the count condition

print(sum)    


# # 8. Write a python program to implement arithmetic operations using nested if statement.

# In[61]:


n1 = int(input('Enter first number : '))
n2 = int(input('Enter second number : '))

print('Select one of the operator to perform')
print('\n Addition (+) \n Subtraction (-) \n Multiplication (*) \n Division (/)')
operator = input('\nEnter the operator : ')

if (operator == '+'):
    result = n1 + n2
    print('\nThe result of {} {} {} = {}'.format(n1, operator, n2, result))
elif (operator == '-'):
    result = n1 - n2
    print('\nThe result of {} {} {} = {}'.format(n1, operator, n2, result))
elif (operator == '*'):
    result = n1 * n2
    print('\nThe result of {} {} {} = {}'.format(n1, operator, n2, result))
elif (operator == '/'):
    result = n1 / n2
    print('\nThe result of {} {} {} = {}'.format(n1, operator, n2, result))
else:
    print('\nPlease select from the listed operators only!')


# # 9. Write a python program to take the temperature in Celsius and convert it to a Fahrenheit.

# In[62]:


Celsius_temp = float(input('Enter the temperature in Celsius : '))

Fahrenheit_temp = (Celsius_temp * 9/5) + 32

print('\nThe temperature in Fahrenheit is', Fahrenheit_temp)


# # 10. Write a python program to find a maximum and minimum number in a list without using an inbuilt function.

# In[63]:


num_list = [39, 78, 44, 13, 22, 65, 32, 49, 35, 8]
print('The list is : ', num_list)
max_number = num_list[0]
min_number = num_list[0]

for i in num_list:
    if i > max_number:
        max_number = i
    elif i < min_number:
        min_number = i

print('\nThe maximum number in the list is : ', max_number)
print('\nThe minimum number in the list is : ', min_number)


# # 11. Write a program in python to print out the number of seconds in 30-day month 30 days, 24 hours in a day, 60 minutes per day, 60 seconds in a minute.

# In[64]:


days_in_30_day_month = 30
hours_in_a_day = 24
minutes_in_an_hour = 60
seconds_in_a_minute = 60

seconds_in_30_day_month = days_in_30_day_month * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
print('\nThe total number of seconds in a 30-day month is :', seconds_in_30_day_month, 'seconds')


# # 12. Write a program in python to print out the number of seconds in a year.

# In[65]:


year = int(input('Enter the year : '))
days_in_a_normal_year = 365
days_in_a_leap_year = 366
hours_in_a_day = 24
minutes_in_an_hour = 60
seconds_in_a_minute = 60

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    days_in_a_year = days_in_a_leap_year 
    print('\nIt is a leap year')
else:
    days_in_a_year = days_in_a_normal_year
    print('\nIt is a normal year')

seconds_in_a_year = days_in_a_year * hours_in_a_day * minutes_in_an_hour * seconds_in_a_minute
print('\nThe total number of seconds in the year {} is : {} seconds'.format(year, seconds_in_a_year))


# # 13. A high-speed train can travel at an average speed of 150 mph, how long will it take a train travelling at this speed to travel from London to Glasgow which is 414 miles away?

# In[66]:


speed = 150  # in mph
distance = 414  # in miles

time = distance / speed

print('\nThe train takes about {} hours to travel from London to Glasgow'.format(time))


# # 14. Write a python program that defines a variable called days_in_each_school_year and assign 192 to the variable. The program should then print out the total hours that you spend in school from year 7 to year 11, if each day you spend 6 hours in school days_in_each_school_year = 192

# In[68]:


days_in_each_school_year = 192
hours_spent_on_each_day = 6
total_hours = 0
hours_spent_in_a_year = hours_spent_on_each_day * days_in_each_school_year

for i in range(7, 12):
    total_hours = total_hours + hours_spent_in_a_year

print('\nThe total hours spend in school from year 7 to year 11 is {} hours'.format(total_hours))


# # 15. If the age of Ram,Sam and Khan are input through the keyboard,write a python program to determine the eldest and youngest of the three.

# In[87]:


Ram_age = int(input('Enter the age of Ram : '))
Sam_age = int(input('Enter  the age of Sam : '))
Khan_age = int(input('Enter the age of Khan : '))

if (Ram_age > Sam_age) and (Ram_age > Khan_age):
    eldest = 'Ram'
    if(Sam_age > Khan_age):
        youngest = 'Khan'
    else:
        youngest = 'Sam'
elif (Sam_age > Ram_age) and (Sam_age > Khan_age):
    eldest = 'Sam'
    if(Ram_age > Khan_age):
        youngest = 'Khan'
    else:
        youngest = 'Ram'    
else:
    eldest = 'Khan'
    if(Ram_age > Sam_age):
        youngest = 'Sam'
    else:
        youngest = 'Ram'    

print('\nThe eldest of the three is', eldest)
print('The youngest of the three is', youngest)


# # 16. Write a python program to rotate a list by right n times with and without slicing technique.

# In[98]:


#  WITH SLICING TECHNIQUE

num_list = [2, 4, 6, 8]
print('\nThe list is', num_list)
n = int(input('\nEnter the value of n : '))
print('\nWITH SLICING TECHNIQUE')
length = len(num_list)
for i in range(0, n):
    if (n<=length):
         rotated_num_list = num_list[-n:] + num_list[:-n]
print("\nThe rotated list with slicing is ", rotated_num_list)


# In[99]:


#  WITHOUT SLICING TECHNIQUE

num_list = [2, 4, 6, 8]
print('\nThe list is', num_list)
n = int(input('\nEnter the value of n : '))
print('\nWITHOUT SLICING TECHNIQUE')
length = len(num_list)
rotated_list = [0] * length
for i in range(0, n):
    rotated_list[(i + n) % length] = num_list[i]
    
print("\nThe rotated list without slicing is ", rotated_num_list)


# # 17. Python program to print the patterns given below:
# 
#   i)
# 
#    1                                                  
#    
#    1  1                                               
#    
#    1  2  1                                            
#    
#    1  3  3  1                                          
#    
#    1  4  6  4  1                                      
#    
#    1  5 10 10 5  1                                    
#     
#    1  6 15 20 15 6  1

# In[73]:


rows = 7
pascal_triangle = []
for line in range(1, rows + 1):
    row = []
    for i in range(line):
        if i == 0 or i == line - 1:
            row.append(1)
        else:
            prev_row = pascal_triangle[line - 2]
            value = prev_row[i - 1] + prev_row[i]
            row.append(value)
    pascal_triangle.append(row)
for row in pascal_triangle:
        for num in row:
            print(num, end=' ')
        print()    


# #  ii)
#     
#     
#        *
#    
#        *  *
#     
#        *  *  *
#    
#        *  *  *  *
#    
#        *  *  *  *  *

# In[76]:


rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print('*', end=' ')
    print()


# #    iii)   
#     
#     
#          *                                   
#                   
#         *  *                                 
#                  
#        *  *  *                                 
#                 
#       *  *  *  *                             
#                
#      *  *  *  *  *                           
#               
#     *  *  *  *  *  *                         
#              
#    *  *  *  *  *  *  *

# In[90]:


rows = 6
for i in range(0, rows):
    for j in range(0, rows - 1):
        print(end=' ')
    rows = rows - 1
    for k in range(0, i + 1):
        print('*', end=' ')
    print()


# #    iv)
#     
#      P
#    
#      Py
#    
#      Pyt
#    
#      Pyth
#    
#      Pytho
#    
#      Python

# In[91]:


String ='Python'
for i in range(0,6):
    print()
    for j in range(0,i+1):
        print(String[j], end=' ')

