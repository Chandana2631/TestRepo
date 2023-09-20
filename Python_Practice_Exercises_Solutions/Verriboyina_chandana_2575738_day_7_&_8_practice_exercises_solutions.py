#!/usr/bin/env python
# coding: utf-8

# # IMPLEMENTATION OF DATA STRUCTURES IN PYTHON

# # 1. Write a Python program to find a target values in a list using linear search with following steps: 
# 
# a. Initialize the list to store the input elements.
# 
# b. Initialize found = False.
# 
# C. Enter the item to be searched (match_item).
# 
# d. For each element in the list
# 
#                           1. if match_item = value
#                                  a. return match_item's position.
# 
# e. If the match_item is not in the list, display an error message that the item is not found in the list.

# In[2]:


# Step a: Initialize the list to store the input elements.
input_list = []
n = int(input('Enter the number of elements in the list: '))
print('Enter the elements one by one :')
for _ in range(n):
    element = int(input())
    input_list.append(element)

# Step b:  Initialize found = False.
found = False

# Step c: Enter the item to be searched (match_item)
match_item = int(input('Enter the item to search for: '))

# Step d: Performing linear search
for position, value in enumerate(input_list):
    if match_item == value:
        found = True
        print('Item', match_item,'is found at position', position)
        break

# Step e: Display error message if the match_item is not in the list.
if not found:
    print('Item', match_item,'is not found in the list.')


# # 2. Write a Python program to implement binary search to find the target values from the list:
# 
# a. Create a separate function to do binary search.
# 
# b. Get the number of inputs from the user.
# 
# c. Store the inputs individually in a list.
# 
# d. In binary search function at first sort the list in order to start the search from middle of the list.
# 
# e. Compare the middle element to right and left elements to search target element.
# 
# f. If greater, move to right of list or else move to another side of the list.
# 
# g. Print the result along with the position of the element.

# In[1]:


# Step a: Create a separate function to do binary search.
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while (left <= right):
        mid = (left + right) // 2

        if (arr[mid] == target):
            return mid  # Target element found at position mid
        elif (arr[mid] < target):
            left = mid + 1  # Target may be in the right half
        else:
            right = mid - 1  # Target may be in the left half

    return -1  # Target element not found in the list

# Step b: Get the number of inputs from the user
n = int(input('Enter the number of elements: '))

# Step c: Store the inputs individually in a list
input_list = []
print('Enter the elements: ')
for _ in range(n):
    element = int(input())
    input_list.append(element)

# Step d: Sort the list for binary search
input_list.sort()

# Step e: Prompt the user for the target element
target = int(input('Enter the target element to search for: '))

# Step f: Perform binary search
result = binary_search(input_list, target)

# Step g: Print the result
if result != -1:
    print('Item', target,'is found at position', result)
else:
    print('Item', target,'is not found in the list.')


# # 3. Write a Python program for sorting a list of elements using selection sort algorithm:
# 
# a. Assume two lists: Sorted list- Initially empty and Unsorted List- Given input list.
# 
# b. In the first iteration, find the smallest element in the unsorted list and place it in the sorted
# 
# list.
# 
# c. In the second iteration, find the smallest element in the unsorted list and place it in the correct position by comparing with the element in the sorted list. 
# 
# d. In the third iteration, again find the smallest element in the unsorted list and place it in the correct position by comparing with the elements in the sorted list.
# 
# e. This process continues till the unsorted list becomes empty.
# 
# f. Display the sorted list.

# In[2]:


def selection_sort(unsorted_list):
    sorted_list = []

    while unsorted_list:
        # Find the minimum element in the remaining unsorted list
        min_index = 0
        for i in range(1, len(unsorted_list)):
            if unsorted_list[i] < unsorted_list[min_index]:
                min_index = i

        # Add the minimum element to the sorted list and remove it from the unsorted list
        sorted_list.append(unsorted_list.pop(min_index))
    return sorted_list

# Get user input for the list of elements
input_list = []
n = int(input('Enter the number of elements: '))
for i in range(n):
    element = int(input('Enter element {}: '.format(i + 1)))
    input_list.append(element)

# Call selection_sort to sort the list
sorted_result = selection_sort(input_list)

# Display the sorted list
print('The Sorted List is :', sorted_result)


# # 4. Write a Python program for sorting a list of elements using insertion sort algorithm:
# 
# a. Assume two lists: Sorted list- Initially empty and Unsorted List- Given input list. 
# 
# b. In the first iteration, take the first element in the unsorted list and insert it in Sorted list.
# 
# c. In the second iteration, take the second element in the given list and compare with the element in the sorted sub list and place it in the correct position.
# 
# d. In the third iteration, take the third element in the given list and compare with the elements in the sorted sub list and place the elements in the correct position.
# 
# e. This process continues until the last element is inserted in the sorted sub list.
# 
# f. Display the sorted elements.

# In[3]:


def insertion_sort(unsorted_list):
    for i in range(1, len(unsorted_list)):
        current_element = unsorted_list[i]
        j = i - 1

        while j >= 0 and current_element < unsorted_list[j]:
            unsorted_list[j + 1] = unsorted_list[j]
            j -= 1

        unsorted_list[j + 1] = current_element

# Get user input for the list of elements
input_list = []
n = int(input('Enter the number of elements: '))
for i in range(n):
    element = int(input('Enter element {}: '.format(i + 1)))
    input_list.append(element)

# Call insertion_sort to sort the list
insertion_sort(input_list)

# Display the sorted list
print('The Sorted List is :', input_list)


# # 5. Write a Python program that performs merge sort on a list of numbers: 
# 
# a. Divide: If the given array has zero or one element, return.
# 
#              i.  Otherwise
#              ii. Divide the input list in to two halves each containing half of the elements. i.e. left half and right half.
# 
# b. Conquer: Recursively sort the two lists (left half and right half).
# 
#               a. Call the merge sort on left half.
#               b. Call the merge sort on right half.
# 
# c. Combine: Combine the elements back in the input list by merging the two sorted lists into a sorted sequence.

# In[4]:


def merge_sort(arr):
    if len(arr) > 1:
        # Divide the input list into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back into the original list
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Get user input for the list of numbers
input_list = []
n = int(input('Enter the number of elements: '))
for i in range(n):
    element = int(input('Enter element {}: '.format(i + 1)))
    input_list.append(element)

# Call merge_sort to sort the list
merge_sort(input_list)

# Display the sorted list
print('The Sorted List is :', input_list)


# # 6. Write a Python script to perform the following operations on a singly linked list
# 
# a. Create a list
# 
# b. Find the smallest element from the list
# 
# c. Insert an element if it is not a duplicate element
# 
# d. Display the elements in reverse order

# In[8]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def find_smallest(self):
        if not self.head:
            return None
        current = self.head
        smallest = current.data
        while current:
            if current.data < smallest:
                smallest = current.data
            current = current.next
        return smallest

    def insert_if_not_duplicate(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current:
                if current.data == data:
                    print('The element already exists in the list')
                    return  # Element is already in the list, don't insert
                if current.next is None:
                    current.next = Node(data)
                    return
                current = current.next

    def display_reverse(self):
        def _display_reverse(node):
            if node is None:
                return
            _display_reverse(node.next)
            print(node.data, end=" ")

        _display_reverse(self.head)

# Create an empty singly linked list
linked_list = SinglyLinkedList()

# Get user input for list creation
n = int(input('Enter the number of elements in the list: '))
print('Enter the elements one by one: ')
for _ in range(n):
    element = int(input())
    linked_list.append(element)

# Find the smallest element
smallest_element = linked_list.find_smallest()
print('The Smallest element is :', smallest_element)

# Get user input for element insertion
element_to_insert = int(input("Enter an element to insert if it's not a duplicate: "))
linked_list.insert_if_not_duplicate(element_to_insert)

# Display elements in reverse order
print('\nThe Elements in reverse order is :')
linked_list.display_reverse()


# # 7. Write a python program to implement the various operations for Stack ADT
# 
# i.) Push ii.) Pop iii.) Display.

# In[9]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty, cannot pop')

    def display(self):
        for item in reversed(self.items):
            print(item, end=" ")
        print()

# Create an empty stack
stack = Stack()

while True:
    print('\nStack Operations :')
    print('1. Push')
    print('2. Pop')
    print('3. Display')
    print('4. Quit')
    
    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        item = input('Enter item to push onto the stack: ')
        stack.push(item)
        print(item,'is pushed onto the stack.')
    elif choice == '2':
        try:
            item = stack.pop()
            print('Popped item:', item)
        except Exception as e:
            print(e)
    elif choice == '3':
        print('Stack elements:')
        stack.display()
    elif choice == '4':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please select a valid option.')


# # 8. Write a python script to implement the various operations for Queue ADT
# 
# i.) Insert ii.) Delete iii.) Display.

# In[10]:


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def insert(self, item):
        self.items.append(item)

    def delete(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise Exception('Queue is empty, cannot delete')

    def display(self):
        for item in self.items:
            print(item, end=" ")
        print()

# Create an empty queue
queue = Queue()

while True:
    print('\nQueue Operations:')
    print('1. Insert')
    print('2. Delete')
    print('3. Display')
    print('4. Quit')
    
    choice = input('Enter your choice (1/2/3/4): ')

    if choice == '1':
        item = input('Enter item to insert into the queue: ')
        queue.insert(item)
        print(item,'is inserted into the queue.')
    elif choice == '2':
        try:
            item = queue.delete()
            print('Deleted item:', item)
        except Exception as e:
            print(e)
    elif choice == '3':
        print('Queue elements:')
        queue.display()
    elif choice == '4':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please select a valid option.')


# # 9. Write a program in python to convert the following infix expression to its postfix form using push and pop operations of a Stack
# 
# a. A/B^C+D*E-F*G
# 
# b. (B^2-4*A*C)^(1/2)(100)

# In[11]:


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise Exception('Stack is empty, cannot pop')

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

# Function to determine the precedence of operators
def precedence(operator):
    if operator in ('+', '-'):
        return 1
    elif operator in ('*', '/'):
        return 2
    elif operator == '^':
        return 3
    return 0  # Default for non-operators

# Function to convert infix expression to postfix
def infix_to_postfix(infix_expression):
    stack = Stack()
    postfix = []
    operators = '+-*/^'

    for char in infix_expression:
        if char.isalnum():
            postfix.append(char)  # Operand, add to postfix
        elif char in operators:
            # Operator, pop higher or equal precedence operators from stack
            while (not stack.is_empty() and
                   precedence(char) <= precedence(stack.peek())):
                postfix.append(stack.pop())
            stack.push(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            # Pop operators from stack until '(' is encountered
            while (not stack.is_empty() and stack.peek() != '('):
                postfix.append(stack.pop())
            stack.pop()  # Pop the '('

    # Pop remaining operators from stack
    while not stack.is_empty():
        postfix.append(stack.pop())

    return ''.join(postfix)

# Test the infix to postfix conversion
infix_expression_a = 'A/B^C+DE-FG'
infix_expression_b = '(B^2-4AC)^(1/2)(100)'

postfix_a = infix_to_postfix(infix_expression_a)
postfix_b = infix_to_postfix(infix_expression_b)

print('The Infix Expression for A is :', infix_expression_a)
print('The Postfix Expression for A is :', postfix_a)

print('\nThe Infix Expression for B is :', infix_expression_b)
print('The Postfix Expression for B is :', postfix_b)

