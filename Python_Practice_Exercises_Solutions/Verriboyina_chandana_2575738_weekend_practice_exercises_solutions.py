#!/usr/bin/env python
# coding: utf-8

# # WEEKEND ASSIGNMENTS

# # 1. Case Study: Online Shopping Cart Exception Handling
# 
# You are working as a Python developer for an e-commerce company, and your team is responsible for building and maintaining the shopping cart module of the website. Customers can add items to their cart, view the cart contents, and proceed to checkout.
# 
# Recently, there have been reports of unexpected crashes and errors when customers interact with their shopping carts. Your task is to investigate these issues and improve the exception handling in the shopping cart code to make it more robust.
# 
# Requirements and Scenarios:
# 
# Scenario 1 - Adding Items to Cart:
# 
# When a customer adds an item to their cart, they provide the product ID and quantity. Handle exceptions that may occur during this process, such as:
# 
#            i)   Product ID not found in the product catalog.
#            ii)  Invalid quantity (e.g., negative quantity or non-integer input).
# 
# Scenario 2 - Viewing Cart Contents:
# 
# When a customer views their cart, display the list of items and their quantities. Handle exceptions that may occur during this process, such as:
# 
#            i)   Empty cart (no items added).
#            ii)  Unexpected errors (e.g., network issues when fetching cart data).
# 
# Scenario 3 - Proceeding to Checkout:
# 
# When a customer proceeds to checkout, validate the cart and process the payment. Handle exceptions that may occur during this process, such as:
# 
#            i)   Insufficient stock for some items in the cart.
#            ii)  Payment gateway errors.
#            iii) Customer payment method declined
# 
# Your Tasks:
# 
# 1. Review the existing shopping cart code to identify potential areas where exceptions may occur.
# 
# 2. Enhance the exception handling in the code by adding appropriate try, except, and finally blocks to handle exceptions gracefully. Provide helpful error messages to the user where applicable.
# 
# 3. Ensure that the program continues to run smoothly even when exceptions occur, and customers receive informative feedback.
# 
# 4. Test the shopping cart thoroughly with different scenarios to ensure that it handles exceptions correctly.

# In[1]:


import mysql.connector

class ShoppingCart:
    def __init__(self):
        self.cart = {}
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Chandana@2631",
            database="ecommerce"
        )
        self.cursor = self.db.cursor()
    # Scenario 1 - Adding Items to Cart
    def add_to_cart(self, product_id, quantity):
        try:
            # Check product existence and stock in the database
            self.cursor.execute("SELECT name, stock FROM products WHERE id = %s", (product_id,))
            product_data = self.cursor.fetchone()
            if not product_data:
                raise ValueError("Invalid product ID. Please choose a valid product.")
            product_name, product_stock = product_data

            if quantity <= 0 or not isinstance(quantity, int):
                raise ValueError("Invalid quantity. Please enter a positive integer.")
            if quantity > product_stock:
                raise ValueError("Insufficient stock for the selected product.")

            if product_id in self.cart:
                self.cart[product_id] += quantity
            else:
                self.cart[product_id] = quantity
            print(f"Added {quantity} of {product_name} to the cart.")
        except ValueError as e:
            print(f"Error: {e}")
    # Scenario 2 - Viewing Cart Contentss
    def view_cart(self):
        try:
            if not self.cart:
                print("Your cart is empty.")
            else:
                print("Cart Contents:")
                for product_id, quantity in self.cart.items():
                    # Fetch the product name from the database
                    self.cursor.execute("SELECT name FROM products WHERE id = %s", (product_id,))
                    product_name = self.cursor.fetchone()[0]
                    print(f"{product_name} (Quantity: {quantity})")
  
        except Exception as e:
            print(f"Error: {e}")

    # Scenario 3 - Proceeding to Checkout       
    def checkout(self):
        try:
            if not self.cart:
                raise ValueError("Your cart is empty. Nothing to checkout.")
        
            for product_id, quantity in self.cart.items():
            # Check if there's enough stock in the database
                self.cursor.execute("SELECT stock FROM products WHERE id = %s", (product_id,))
                product_stock = self.cursor.fetchone()[0]
                if quantity > product_stock:
                    raise ValueError(f"Insufficient stock for {self.get_product_name(product_id)}.")
            
            # Deduct the ordered quantity from the product's stock in the database
                updated_stock = product_stock - quantity
                self.cursor.execute("UPDATE products SET stock = %s WHERE id = %s", (updated_stock, product_id))
        
        # Placeholder for payment gateway logic
            payment_successful = self.process_payment()  # Implement your payment gateway here

            if payment_successful:
                print("Checkout successful! Thank you for your purchase.")
                self.cart = {}  # Empty the cart after successful checkout
            else:
                raise ValueError("Payment processing failed. Please try again later.")
        except ValueError as e:
            print(f"Error: {e}")

    def process_payment(self):
        try:
        # Connect to a payment gateway API (This is a placeholder)
            payment_gateway_response = self.connect_to_payment_gateway()

        # Check the response to determine if the payment was successful
            if payment_gateway_response == "success":
                return True
            else:
                return False
        except Exception as e:
            print(f"Payment processing error: {e}")
            return False

    def connect_to_payment_gateway(self):
    # Here, we're just simulating a successful payment for demonstration purposes.
        return "success"

def main():
    cart = ShoppingCart()
    while True:
        print("\nOptions:")
        print("1. Add to Cart")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            product_id = int(input("Enter the product ID: "))
            quantity = int(input("Enter the quantity: "))
            cart.add_to_cart(product_id, quantity)
        elif choice == "2":
            cart.view_cart()
        elif choice == "3":
            cart.checkout()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()


# # 2. Create a Python function that checks if two given strings are anagrams of each other.
# 

# In[3]:


def anagram(str1, str2):

    # Convert both strings to lowercase.
    str1 = str1.lower()
    str2 = str2.lower()

    # Compare the sorted strings.
    if sorted(str1) == sorted(str2):
        print(str1,'and',str2,'are anagrams.')
    else:
        print(str1,'and',str2,'are not anagrams.')
str1 = input('Enter string 1 : ')
str2 = input('Enter string 2 : ')
anagram(str1, str2)


# # 3. Create a Python function that checks if two given strings are anagrams of each other.

# In[1]:


# IT IS A REPEATED QUESTION OF 2 AS PER WEEKEND ASSIGNMENTS PDF

def anagram(str1, str2):

    # Convert both strings to lowercase.
    str1 = str1.lower()
    str2 = str2.lower()

    # Compare the sorted strings.
    if sorted(str1) == sorted(str2):
        print(str1,'and',str2,'are anagrams.')
    else:
        print(str1,'and',str2,'are not anagrams.')
str1 = input('Enter string 1 : ')
str2 = input('Enter string 2 : ')
anagram(str1, str2)


# # 4. Case Study: Online Bookstore Database Connectivity
# 
# You are a Python developer working on the backend of an online bookstore website. The website's database stores information about books, customers, orders, and inventory. Your task is to develop and maintain the database connectivity and interaction components.
# 
# Requirements and Scenarios:
# 
# Scenario 1 - Customer Registration:
# 
# When a new customer registers on the website, their information (name, email, password) should be stored in the database.
# Handle exceptions that may occur during the registration process, such as:
# 
#                1. Duplicate email addresses.
#                2. Database connection errors.
# 
# Scenario 2 - Book Inventory Management:
# 
# Implement functionality to add new books to the inventory, update existing book details, and delete books.
# Handle exceptions that may occur during these operations, such as:
# 
#                1. Invalid book data.
#                2. Database errors when updating or deleting books.
# 
# Scenario 3 - Customer Orders:
# 
# Allow customers to place orders for books. Each order includes customer details and a list of ordered books.
# Handle exceptions that may occur during order placement, such as:
# 
#                1. Insufficient stock for some books.
#                2. Database errors when recording orders.
# 
# Scenario 4 - Order History:
# 
# Customers should be able to view their order history, which includes details of past orders.
# Handle exceptions that may occur when retrieving order history, such as:
# 
#                1. No orders found for the customer.
#                2. Database connection issues.
# Your Tasks:
# 
# 1. Review the existing database interaction code to identify potential areas where exceptions may occur.
# 
# 2. Enhance the exception handling in the code by adding appropriate try, except, and finally blocks to handle exceptions gracefully. Provide helpful error messages to the user where applicable.
# 
# 3. Ensure that the program continues to run smoothly even when exceptions occur, and customers receive informative feedback.
# 
# 4. Implement database queries and transactions following best practices to maintain data integrity.
# 
# 5. Test the website's database interactions thoroughly with different scenarios to ensure that it handles exceptions correctly.

# In[4]:


import mysql.connector

class OnlineBookstore:
    def __init__(self):
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Chandana@2631",
            database="bookstore"
        )
        self.cursor = self.db.cursor()

    def register_customer(self, name, email, password):
        try:
            # Check for duplicate email
            self.cursor.execute("SELECT id FROM customers WHERE email = %s", (email,))
            existing_customer = self.cursor.fetchone()
            if existing_customer:
                raise ValueError("Email address is already registered.")

            # Insert new customer
            insert_query = "INSERT INTO customers (name, email, password) VALUES (%s, %s, %s)"
            self.cursor.execute(insert_query, (name, email, password))
            self.db.commit()

            print("Registration successful.")
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        except ValueError as e:
            print(f"Registration Error: {e}")

    def add_book(self, title, author, price, stock):
        try:
            # Insert new book
            insert_query = "INSERT INTO books (title, author, price, stock) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(insert_query, (title, author, price, stock))
            self.db.commit()

            print("Book added to inventory.")
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")

    def place_order(self, customer_id, book_id, quantity):
        try:
            # Check book stock
            self.cursor.execute("SELECT stock FROM books WHERE id = %s", (book_id,))
            book_stock = self.cursor.fetchone()[0]
            if quantity > book_stock:
                raise ValueError("Insufficient stock for the selected book.")

            # Insert new order
            insert_query = "INSERT INTO orders (customer_id, book_id, quantity) VALUES (%s, %s, %s)"
            self.cursor.execute(insert_query, (customer_id, book_id, quantity))

            # Update book stock
            new_stock = book_stock - quantity
            self.cursor.execute("UPDATE books SET stock = %s WHERE id = %s", (new_stock, book_id))

            self.db.commit()

            print("Order placed successfully.")
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")
        except ValueError as e:
            print(f"Order Error: {e}")

    def get_order_history(self, customer_id):
        try:
            # Retrieve order history for the customer
            self.cursor.execute("SELECT o.order_id, b.title, o.quantity, o.order_date FROM orders o JOIN books b ON o.book_id = b.id WHERE o.customer_id = %s", (customer_id,))
            order_history = self.cursor.fetchall()

            if not order_history:
                print("No orders found for this customer.")
            else:
                print("Order History:")
                for order in order_history:
                    order_id, book_title, quantity, order_date = order
                    print(f"Order ID: {order_id}, Book: {book_title}, Quantity: {quantity}, Date: {order_date}")
        except mysql.connector.Error as e:
            print(f"Database Error: {e}")

    def close_db_connection(self):
        self.cursor.close()
        self.db.close()

def main():
    bookstore = OnlineBookstore()

    while True:
        print("\nOptions:")
        print("1. Register Customer")
        print("2. Add Book to Inventory")
        print("3. Place Order")
        print("4. Get Order History")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter customer name: ")
            email = input("Enter customer email: ")
            password = input("Enter customer password: ")
            bookstore.register_customer(name, email, password)
        elif choice == "2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            stock = int(input("Enter book stock: "))
            bookstore.add_book(title, author, price, stock)
        elif choice == "3":
            customer_id = int(input("Enter customer ID: "))
            book_id = int(input("Enter book ID: "))
            quantity = int(input("Enter quantity: "))
            bookstore.place_order(customer_id, book_id, quantity)
        elif choice == "4":
            customer_id = int(input("Enter customer ID: "))
            bookstore.get_order_history(customer_id)
        elif choice == "5":
            bookstore.close_db_connection()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")
main()


# # QUESTION 5 : NUMBERING FOR FIFTH QUESTION IS MISSED AND WAS NOT GIVEN AS PER WEEKEND ASSIGNMENTS PDF, SO 6TH QUESTION FOLLOWS BY!

# # 6. Read a text file containing a list of names or numbers, sort the data, and write the sorted data back to a new file.

# In[10]:


input_file_path = input('Enter input file : ')
output_file_path = input('Enter output file : ')
try:    
    # Open the input text file for reading.
    with open(input_file_path, 'r') as input_file:
        lines = input_file.readlines()

    # Sort the list of lines.
    lines.sort()

    # Open a new text file for writing.
    with open(output_file_path, 'w') as output_file:
        for line in lines:
            output_file.write(line)
    print('The list of names or numbers are sorted and returned back to the new output file.')
    
except FileNotFoundError:
    print('The file', input_file_path,'was not found.')
except Exception as e:
    print('Error:', e)


# # 7. Write a Python script that compares two text files and identifies the differences between them, including added, modified, and deleted lines.

# In[43]:


def compare_text_files(file1_path, file2_path):
    try:
        with open(file1_path, 'r', encoding='utf-8') as file1, open(file2_path, 'r', encoding='utf-8') as file2:
            file1_lines = file1.readlines()
            file2_lines = file2.readlines()

        Added_lines = [line for line in file2_lines if line not in file1_lines]
        Deleted_lines = [line for line in file1_lines if line not in file2_lines]
        Modified_lines = [line for line in file2_lines if line not in file1_lines]

        print("\nAdded Lines:")
        for line in Added_lines:
            print(line, end='')

        print("\n\nDeleted Lines:")
        for line in Deleted_lines:
            print(line, end='')

        print("\n\nModified Lines:")
        for line in Modified_lines:
            print(line, end='')
        print('\n\nThe differences were identified between them.')
    
    except FileNotFoundError:
        print('The provided file(s) were not found.')
    except Exception as e:
        print('Error:', e)
    
file1_path = input('Enter the first text file: ')
file2_path = input('Enter the second text file: ')
compare_text_files(file1_path, file2_path)


# # 8. Develop a Python program that compresses a large text file using a compression algorithm (e.g., gzip) and then decompresses it back to its original form.

# In[44]:


import gzip
import shutil
try:
    # Replace with your large text file path        
    input_file = input('Enter the input file: ')  
    compressed_file = input('Enter the compressed file: ')
    decompressed_file = input('Enter the decompressed file: ')
    
    # Compress the input file
    print('\nCompressing ',input_file,'to',compressed_file,'...')
    with open(input_file, 'rb') as f_input, gzip.open(compressed_file, 'wb') as f_output:
        shutil.copyfileobj(f_input, f_output)
    print('Compression completed.')

    # Decompress the compressed file
    print('\nDecompressing ',compressed_file,'to',decompressed_file,'...')
    with gzip.open(compressed_file, 'rb') as f_input, open(decompressed_file, 'wb') as f_output:
        shutil.copyfileobj(f_input, f_output)
    print('Decompression completed.')
    
    # Handles errors and exceptions
except FileNotFoundError:
    print('The provided file(s) were not found.')
except Exception as e:
    print('Error:', e)


# # 9. Read a binary file (e.g., an image or audio file) in Python and perform an operation, such as resizing an image or modifying audio data.

# In[2]:


#READING A BINARY FILE I.E., AN IMAGE FILE
from PIL import Image

# Open the image file
pic_input = input('Enter the name of picture in jpg : ')
input_image = Image.open(pic_input)

# Resize the image to a new width and height
new_width = int(input('Enter width size : '))
new_height = int(input('Enter height size : '))
resized_image = input_image.resize((new_width, new_height))

# Save the resized image
resized_image.save('new_image.jpg')
print('\nThe picture is resized with the given dimensions.')


# # 10. Write a python program to Combine the contents of multiple text files into a single file using Python. Each file should be appended to the end of the resulting file.

# In[3]:


try:
    n = int(input('Enter the number of files to combine : '))
    input_files = []
    for i in range(n):
        file_name = input('Enter the name of file {}: '.format(i + 1))
        input_files.append(file_name)
    output_file = input('Enter the output file to be stored : ')
        
    with open(output_file, 'w') as output:
        for file_name in input_files:
            with open(file_name, 'r') as input_file:
                output.write(input_file.read())
                output.write("\n")
    print('\nThe process of combining the contents of multiple text files into a single file is done successfully.')
    
except FileNotFoundError:
    print('The provided file(s) were not found.')
except Exception as e:
    print('Error:', e)


# # 11. Create a Python script that accepts a text file as a command-line argument and counts the number of words, lines, and characters in the file.
# 

# In[ ]:


# weekQ11.py

import argparse

def count_words_lines_characters(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            
            # Count the number of words (split by whitespace)
            word_count = len(text.split())

            # Count the number of lines (split by newline characters)
            line_count = text.count('\n') + 1  # Adding 1 to account for the last line without a newline character
            
            # Count the number of characters
            char_count = len(text)
        return word_count, line_count, char_count
    
    except Exception as e:
        return None

# Create command-line argument parser
parser = argparse.ArgumentParser(description = 'Count words, lines, and characters in a text file.')

# Define command-line argument
parser.add_argument('file_path', help = 'Path to the text file')

# Parse command-line arguments
args = parser.parse_args()

# Call the count_words_lines_characters function
result = count_words_lines_characters(args.file_path)

if result:
    word_count, line_count, char_count = result
    print('Number of words:', word_count)
    print('Number of lines:', line_count)
    print('Number of characters:', char_count)
else:
    print('An error has occurred while processing the file.')


# In[25]:


# By giving the below command we can run the 'weekQ11' module in Jupyter Notebook cell

get_ipython().system('python weekQ11.py apple.txt')


# # 12. Build a command-line calculator that accepts a mathematical expression as a string argument and evaluates it, then prints the result.

# In[ ]:


# calculator_operation.py

import argparse

def calculator_operation(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        return 'Error:' + e

# Create command-line argument parser
parser = argparse.ArgumentParser(description = 'Command-line calculator that evaluates a mathematical expression.')

# Define command-line argument
parser.add_argument('expression', help = 'Mathematical expression to evaluate')

# Parse command-line arguments
args = parser.parse_args()

# Call the calculate function
result = calculator_operation(args.expression)

# Print the result
print('The result for the given mathematical expression is:', result)


# In[27]:


# By giving the below command we can run the 'calculator' module in Jupyter Notebook cell

get_ipython().system('python calculator.py "8 * 8"')


# # 13. Implement a Python script that takes a CSV file and two column names as command-line arguments. The script should calculate the average of values in one column and store the result in another column in the same file.

# In[ ]:


import pandas as pd
import argparse

# Calculating the average and updating the CSV file
def calculate_average(inputfile_csv, column_to_average, result_avg_column):
    try:
        # Reading the CSV file into a DataFrame
        df = pd.read_csv(inputfile_csv)

        # Calculating the average of the specified column
        average = df[column_to_average].mean()

        # Adding a new column with the average value
        df[result_avg_column] = average

        # Writing the updated DataFrame back to the CSV file
        df.to_csv(inputfile_csv, index = False)

        print('The average of', column_to_average,'is :', average)
        print('The column {} is updated with the average value of column {} in the CSV file'.format(result_avg_column, column_to_average))

    except Exception as e:
        print('An error occurred:', e)
        
parser = argparse.ArgumentParser(description = 'Calculate the average of values in a CSV column and store the result in another column.')
parser.add_argument('inputfile_csv', help = 'Path to the input CSV file')
parser.add_argument('column_to_average', help = 'Name of the column to calculate the average for')
parser.add_argument('result_avg_column', help = 'Name of the column to store the average result')

args = parser.parse_args()
calculate_average(args.inputfile_csv, args.column_to_average, args.result_avg_column)


# In[7]:


# By giving the below command we can run the 'calculate_average' module in Jupyter Notebook cell

get_ipython().system('python calculate_average.py marks.csv Marks Average_marks')


# # 14. Write a Python script that takes two integer command-line arguments and prints their sum.

# In[ ]:


# sum.py

import argparse

def add_two_integers(num1, num2):
    return num1 + num2

# Create command-line argument parser
parser = argparse.ArgumentParser(description = 'Add two integers.')

# Define command-line arguments
parser.add_argument('num1', type = int, help = 'First integer')
parser.add_argument('num2', type = int, help = 'Second integer')

# Parse command-line arguments
args = parser.parse_args()

# Call the add_two_numbers function
result = add_two_integers(args.num1, args.num2)

# Print the result
print('The sum of {} and {} is {}'.format(args.num1, args.num2, result))


# In[28]:


# By giving the below command we can run the 'sum' module in Jupyter Notebook cell

get_ipython().system('python sum.py 23 27')


# # 15. Create a custom Python module that includes functions to calculate the factorial of a number and to check if a number is prime. Import and use this module in another Python script.

# In[ ]:


# Custom module 'fact_prime.py'

def factorial(n):
    if (n < 0):
        return False
    elif (n == 0):
        return 1
    else:
        return n * factorial(n - 1)

def prime(n):
    if (n <= 1):
        return False
    for i in range(2, int(n**0.5) + 1):
        if (n % i == 0):
            return False
    return True


# In[3]:


import fact_prime

num = int(input('Enter the number : '))
fact = fact_prime.factorial(num)
print('\nThe factorial of',num,'is :', fact)

# Checking if a number is prime or not
if fact_prime.prime(num):
    print('\n',num,'is a prime number')
else:
    print('\n',num,'is not a prime number')


# # 16. Create a Python module named calculator.py that contains functions for each of the four operations (addition, subtraction, multiplication, and division). Each function should take two arguments, perform the respective operation, and return the result.

# In[ ]:


# module 'calculator' code

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Error: Division by zero.'
    return a / b


# In[5]:


import calculator

number1 = int(input('Enter the first number : '))
number2 = int(input('Enter the second number : '))

addition = calculator.add(number1, number2)
subtraction = calculator.subtract(number1, number2)
multiplication = calculator.multiply(number1, number2)
division = calculator.divide(number1, number2)

print('\nThe addition of {} and {} is : {}'.format(number1, number2, addition))
print('The subtraction of {} and {} is : {}'.format(number1, number2, subtraction))
print('The multiplication of {} and {} is : {}'.format(number1, number2, multiplication))
print('The division of {} and {} is : {}'.format(number1, number2, division))

