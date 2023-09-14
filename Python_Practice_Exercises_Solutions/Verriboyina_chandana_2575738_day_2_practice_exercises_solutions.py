#!/usr/bin/env python
# coding: utf-8

# # FUNCTIONS

# # 1. Write a python Function to list even and odd numbers in a list.

# In[1]:


def list_even(num):
    even_numbers = []
    for i in num:
        if (i % 2) == 0:
            even_numbers.append(i)
    return even_numbers        
def list_odd(num):
    odd_numbers = []
    for j in num:
        if (j % 2) != 0:
            odd_numbers.append(j)
    return odd_numbers

num_list = [10, 11, 12, 13, 14, 15, 16, 17, 18]
even = list_even(num_list) 
odd = list_odd(num_list)

print('\nList of even numbers :', even)
print('\nList of even numbers :', odd)


# # 2. Write and run a Python program that asks the user to enter 8 integers (one at a time), and then prints out how many of those integers were even numbers. For example, if the user entered 19, 6, 9, 20, 13, 7, 6, and 1, then your program should print out 3 since 3 of those numbers were even.

# In[2]:


count = 0

for i in range(0,8):
    number = int(input('Enter the integer : '))
    if (number % 2) == 0:
        count = count + 1

print('The total count of even integers entered is', count)


# # 3. Write a Python program where you take any positive integer n, if n is even, divide it by 2 to get n/ 2. If n is odd, multiply it by 3 and add 1 to obtain 3n+ 1. Repeat the process until you reach 1.

# In[10]:


def collatz(n):
    while (n != 1):
        print(n, end=' ')
        if (n % 2 == 0):
            n = n // 2
        else:
            n = (3 * n)+ 1        
    print(1)

n = int(input('\nEnter a positive integer : '))
if (n <= 0):
    print('Please give a positive integer')
else:
    print('\nThe Collatz sequence is:', end=' ')
    collatz(n)


# # 4. Write a Python program to compute the sum of all the multiples of 3 or 5 below 500.

# In[12]:


sum = 0
for i in range(1, 500):
    if (i % 3 == 0) or (i % 5 == 0):
        sum = sum + i
print('\nThe sum of all the multiples of 3 or 5 below 500 is :', sum)


# # 5. To write a Python program to find first 'n' prime numbers from a list of given numbers.

# In[51]:


def is_prime(num):
    if (num<=1):
        return False
    for i in range(2, int(num**0.5) + 1): 
        if (num % i == 0):
            return False
    return True

def find_primes(numbers, n): 
    prime_numbers = []   
    for num in numbers: 
        if is_prime(num):
            prime_numbers.append(num)
        if len(prime_numbers) == n: 
            break
    return prime_numbers

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print('The original list is :', num_list)
n = int(input('\nEnter the value of n : '))

prime_list =find_primes(num_list, n)
print('\nThe first', n,'prime numbers from the original list is :', prime_list)


# # 6. To write a Python program to compute matrix multiplication.

# In[55]:


def matrix_multiplication(A, B):
    if len(A[0])!=len(B):
        raise Error('Matrix dimensions are not matched for multiplication') 
    result = [[0 for x in range(len(B[0]))] for x in range(len(A))] 
    for i in range(len(A)): 
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]
    return result

A = [[1, 2], [4, 5]]
B = [[7, 8], [9, 10]] 
product = matrix_multiplication(A, B) 
print('The result matrix is :\n')
for r in product: 
    print(r)


# # 7. Write a python Function to count the number of vowels in a string.

# In[13]:


def vowels(String):
    vowels = 'AEIOUaeiou'
    vowel_count = 0
    for char in String:
        if char in vowels:
            vowel_count = vowel_count + 1
    return vowel_count

String = 'Welcome to python'
vowel_count = vowels(String)
print('\nThe number of vowels in the String is :',vowel_count)


# # 8. Write a python Function for finding factorial for the given number using a recursive function.

# In[58]:


def factorial(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return n * factorial(n - 1)

n = int(input('\nEnter the number : '))
fact = factorial(n)
print('\nThe factorial of {} is {}'.format(n, fact))


# # 9. Write a python Function for generating the Fibonacci series using the function. 

# In[61]:


def fibonacci(n):
    if (n <= 0):
        return []
    elif (n == 1):
        return [0]
    elif (n == 2):
        return [0, 1]
    else:
        f_series = fibonacci(n - 1)
        f_series.append(f_series[-1] + f_series[-2])
        return f_series
    
n = int(input('\nEnter the number : '))
fibonacci_series = fibonacci(n)
print('\nThe fibonacci series is', fibonacci_series)


# # 10. Python program to display the given integer in reverse order using the function without an in-built function.

# In[73]:


number = int(input('\nEnter the number : ')) 
rev_num = 0

while number != 0:
    digit = number % 10
    rev_num = rev_num * 10 + digit
    number //= 10

print("\nReversed Number: " + str(rev_num))


# # 11. Write a Python Function to display all integers within the range 200-300 whose sum of digits is an even number.

# In[80]:


def sum_of_even(start, end):
    for i in range(start, end + 1):  
        i = str(i)              
        sum = 0                 
        for j in i:           
            j = int(j)          
            sum = sum + j         
        if (sum % 2 == 0):          
            my_list.append(i) 
    return my_list

my_list = [] 
start = 200
end = 300  
sum_of_even_digits_list = sum_of_even(start, end)
print('\nAll integers within the range', start,'to', end,'whose sum of digits is an even number is :\n\n', sum_of_even_digits_list)


# # 12. Write a python Function to find the number of digits and sum of digits for a given integer.

# In[85]:


def find_sum_and_count(number):
    digit_count = 0
    digit_sum = 0
    number = abs(number)
    while (number > 0): 
        digit = number % 10 
        digit_count = digit_count + 1
        digit_sum = digit_sum + digit
        number //= 10 
    return digit_count, digit_sum

number = int(input('\nEnter an integer : ')) 
num_of_digits, sum_of_digits = find_sum_and_count(number)

print('\nThe number of digits :', num_of_digits)
print('\nThe sum of the digits :', sum_of_digits)


# # 13. Write functions called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise and has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

# In[21]:


def is_sorted(input_list):
    return all(input_list[i] <= input_list[i+1] for i in range(len(input_list) - 1))

def has_duplicates(arr):
    seen = []
    for item in arr:
        if item in seen:
            return True
        seen.append(item)
    return False

normal_list = [1, 3, 5, 7, 9, 11]
print('\nThe normal list is : ', normal_list)
print()
if (is_sorted(normal_list)):
    print(is_sorted(normal_list), ', The given normal list is sorted')
else:
    print(is_sorted(normal_list), ', The given normal list is not sorted')
    
duplicate_list = [6, 4, 2, 2, 3, 5]
print('\n\nThe list given to check duplicates is : ', duplicate_list)
print()
if (has_duplicates(duplicate_list)):
    print(has_duplicates(duplicate_list), ', The given list have duplicates in it')  
else:
    print(has_duplicates(duplicate_list), ', The given list do not have duplicates in it') 


# # 14. Write functions called nested_sum that takes a list of integers and adds up the elements from all the nested lists and cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the original list

# In[20]:


def nested_sum(nested_list):
    total = 0
    for sublist in nested_list:
        total += sum(sublist)
    return total

def cumsum(cumsum_list):
    cumulative_sum = [sum(cumsum_list[:i+1]) for i in range(len(cumsum_list))]
    return cumulative_sum

nested_list = [[1, 2, 3], [1, 3, 5], [2, 4, 6]]
print('\nThe list taken for nested sum is : ', nested_list)
nested_list_sum = nested_sum(nested_list)
print('The nested sum of the given list is :', nested_list_sum)

cumsum_list = [1, 2, 3, 4, 5, 6, 7]
print('\nThe list taken for cumulative sum is : ', cumsum_list)
cumsum_list_sum = cumsum(cumsum_list)
print('The nested sum of the given list is :', cumsum_list_sum)

