#!/usr/bin/env python
# coding: utf-8

# # OBJECT ORIENTED PROGRAMMING IN PYTHON

# # 1.a) Write a python program to create a base class "Shape" with methods to calculate area and perimeter. Then, create derived classes "Circle" and "Rectangle" that inherit from the base class and calculate their respective areas and perimeters. Demonstrate their usage in a program.

# In[21]:


import math

# Base class
class Shape:
    def __init__(self):
        pass
    
    def calculate_area(self):
        pass
    
    def calculate_perimeter(self):
        pass

# Derived class for Circle
class Circle(Shape):
    def __init__(self,radius=input('Enter the radius of the circle: ')):
        self.radius = int(radius)
    
    def calculate_area(self):
        return (math.pi * self.radius ** 2)
    
    def calculate_perimeter(self):
        return (2 * math.pi * self.radius)

# Derived class for Rectangle
class Rectangle(Shape):
    def __init__(self, length=input('Enter the length of the rectangle: '), width=input('Enter the width of the rectangle: ')):
        self.length = int(length)
        self.width = int(width)
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

# Demonstrating their usage

# Create instances of Circle and Rectangle
circle = Circle()
rectangle = Rectangle()

# Calculates and displays area and perimeter of the Circle
print('\nIn circle,')
print('Area, A =', circle.calculate_area(),'units')
print('Perimeter, P =', circle.calculate_perimeter(),'units')

# Calculates and displays area and perimeter of the Rectangle
print('\nIn rectangle,')
print('Area, A =', rectangle.calculate_area(),'units')
print('Perimeter, P =', rectangle.calculate_perimeter(),'units')


# # 1.b) You are developing an online quiz application where users can take quizzes on various topics and receive scores.
# 
# 1. Create a class for quizzes and questions.
# 
# 2. Implement a scoring system that calculates the user's score on a quiz.
# 
# 3. How would you store and retrieve user progress, including quiz history and scores?

# In[1]:


class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options
        self.correct_option = correct_option

    def is_correct(self, user_choice):
        return user_choice == self.correct_option

class Quiz:
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def take_quiz(self):
        score = 0
        total_possible_score = len(self.questions)

        for question in self.questions:
            print(question.text)
            for i, option in enumerate(question.options):
                print(f"{i + 1}. {option}")

            user_choice = int(input("Enter your choice (1, 2, 3, etc.): ")) - 1

            if question.is_correct(user_choice):
                score += 1

        return score, total_possible_score

class UserProgress:
    def __init__(self):
        self.quiz_history = {}  # Dictionary to store user's quiz history and scores

    def take_quiz(self, quiz):
        score, total_possible_score = quiz.take_quiz()
        self.quiz_history[quiz.title] = (score, total_possible_score)
        return score

    def get_quiz_history(self):
        return self.quiz_history

# Create questions and a quiz
question1 = Question("Which of the following is the largest continent in the world?", ["Africa", "Europe", "Asia"], 2)
question2 = Question("What is the capital of Germany?", ["London", "Berlin", "Paris"], 1)
quiz1 = Quiz("General Knowledge", [question1, question2])

# Create a user's progress
user_progress = UserProgress()

# Take the quiz and store user progress
user_score = user_progress.take_quiz(quiz1)
print(f"You scored {user_score} out of {len(quiz1.questions)} on the {quiz1.title} quiz.")

# Get and print user's quiz history
quiz_history = user_progress.get_quiz_history()
for quiz_title, (score, total_possible_score) in quiz_history.items():
    print(f"{quiz_title}: Scored {score} out of {total_possible_score}")

# Take another quiz
question3 = Question("What is the sum of all angles in a triangle?", ["90", "180", "360"], 1)
quiz2 = Quiz("Maths", [question3])
user_score = user_progress.take_quiz(quiz2)
print(f"You scored {user_score} out of {len(quiz2.questions)} on the {quiz2.title} quiz.")


# # 2. Write a python script to create a class "Person" with private attributes for age and name. Implement a method to calculate a person's eligibility for voting based on their age. Ensure that age cannot be accessed directly but only through a getter method.

# In[2]:


class Person:
    def __init__(self, name, age):
        self.__name = name  # Private attribute for name
        self.__age = age    # Private attribute for age
    # Getter method for age
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def is_eligible_to_vote(self):
        if (self.__age >= 18):
            return True
        else:
            return False

    def set_age(self, age):
        self.__age = age

# Input from the user
name = input("Enter the name of a person: ")
age = int(input("Enter the person's age: "))

# Create a Person object
person1 = Person(name, age)

# Accessing name and age through getter methods
print("\nName:",person1.get_name())
print("Age:",person1.get_age())

# Checking eligibility to vote
if person1.is_eligible_to_vote():
    print("Yes, Eligible to vote.")
else:
    print("No, Not eligible to vote.")


# # 3. You are tasked with designing a Python class hierarchy for a simple banking system. The system should be able to handle different types of accounts, such as Savings Accounts and Checking Accounts. Both account types should have common attributes like an account number, account holder's name, and balance. However, Savings Accounts should have an additional attribute for interest rate, while Checking Accounts should have an attribute for overdraft limit.
# 
# 1. Create a Python class called BankAccount with the following attributes and methods:
# 
#          a. Attributes: account_number, account holder_name, balance 
#          b. Methods: __init__() (constructor), deposit(), and withdraw()
# 
# 2. Create two subclasses, SavingsAccount and CheckingAccount, that inherit from the BankAccount class.
# 
# 3. Add the following attributes and methods to each subclass:
# 
#          a. SavingsAccount:
# 
#               i.  Additional attribute: interest_rate
#               ii. Method: calculate_interest(), which calculates and adds interest to the account based on the interest rate.
# 
#          b. CheckingAccount:
# 
#               i.  Additional attribute: overdraft_limit
#               ii. Method: withdraw(), which allows withdrawing money up to the overdraft limit (if available) without                             additional fees.
# 
# 4. Write a program that creates instances of both SavingsAccount and CheckingAccount and demonstrates the use of their methods.
# 
# 5. Implement proper encapsulation by making the attributes private where necessary and providing getter and setter methods as needed.
# 
# 6. Handle any potential errors or exceptions that may occur during operations like withdrawals, deposits, or interest calculations.
# 
# 7. Provide comments in your code to explain the purpose of each class, attribute, and method.
# 
# Note: Your code should create instances of the classes, simulate transactions, and showcase the differences between Savings Accounts and Checking Accounts.

# In[8]:


class BankAccount:
    def __init__(self, account_number, account_holder_name, balance=0.0):
        """
        Constructor to initialize a BankAccount object.
        Args:
            account_number (str): The account number.
            account_holder_name (str): The account holder's name.
            balance (float): The initial balance (default is 0.0).
        """
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._balance = balance

    def get_account_number(self):
        # Get the account number.
        return self._account_number

    def get_account_holder_name(self):
        # Get the account holder's name.
        return self._account_holder_name

    def get_balance(self):
        # Get the current balance.
        return self._balance

    def deposit(self, amount):
        """
        Deposit money into the account.
        Args:
            amount (float): The amount to deposit.
        Raises:
            ValueError: If the amount is negative.
        """
        if (amount < 0):
            raise ValueError("Amount to deposit must be non-negative.")
        self._balance += amount

    def withdraw(self, amount):
        """
        Withdraw money from the account.
        Args:
            amount (float): The amount to withdraw.
        Raises:
            ValueError: If the amount is negative.
            InsufficientFundsError: If there are insufficient funds for withdrawal.
        """
        if amount < 0:
            raise ValueError("Amount to withdraw must be non-negative.")
        if amount > self._balance:
            raise InsufficientFundsError("Insufficient funds for withdrawal.")
        self._balance -= amount

class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0.0, interest_rate=0.0):
        """
        Constructor to initialize a SavingsAccount object.
        Args:
            account_number (str): The account number.
            account_holder_name (str): The account holder's name.
            balance (float): The initial balance (default is 0.0).
            interest_rate (float): The interest rate for the account (default is 0.0).
        """
        super().__init__(account_number, account_holder_name, balance)
        self._interest_rate = interest_rate

    def get_interest_rate(self):
        # Get the interest rate for the account.
        return self._interest_rate

    def calculate_interest(self):
        # Calculate and add interest to the account based on the interest rate.
        interest = self._balance * (self._interest_rate / 100)
        self._balance += interest

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance=0.0, overdraft_limit=0.0):
        """
        Constructor to initialize a CheckingAccount object.
        Args:
            account_number (str): The account number.
            account_holder_name (str): The account holder's name.
            balance (float): The initial balance (default is 0.0).
            overdraft_limit (float): The overdraft limit for the account (default is 0.0).
        """
        super().__init__(account_number, account_holder_name, balance)
        self._overdraft_limit = overdraft_limit

    def get_overdraft_limit(self):
        # Get the overdraft limit for the account.
        return self._overdraft_limit

    def withdraw(self, amount):
        """
        Withdraw money from the account, allowing overdraft up to the limit.
        Args:
            amount (float): The amount to withdraw.
        Raises:
            ValueError: If the amount is negative.
            OverdraftError: If the withdrawal exceeds the overdraft limit.
        """
        if amount < 0:
            raise ValueError("Amount to withdraw must be non-negative.")
        if amount > self._balance + self._overdraft_limit:
            raise OverdraftError("Withdrawal exceeds overdraft limit.")
        self._balance -= amount

class InsufficientFundsError(Exception):
    # Exception raised when there are insufficient funds for withdrawal.
    pass

class OverdraftError(Exception):
    # Exception raised when a withdrawal exceeds the overdraft limit.
    pass

# Creating a savings account
savings_account = SavingsAccount("SAV123", "John Doe", balance=1000.0, interest_rate=2.5)
print(f"Savings Account Holder: {savings_account.get_account_holder_name()}")
print(f"Initial Balance: ${savings_account.get_balance()}")
savings_account.calculate_interest()
print(f"Balance after interest: ${savings_account.get_balance()}")

# Deposit to savings account
savings_account.deposit(200.0)
print(f"Balance after deposit: ${savings_account.get_balance()}")

# Creating a checking account
checking_account = CheckingAccount("CHK456", "Jane Smith", balance=500.0, overdraft_limit=200.0)
print(f"Checking Account Holder: {checking_account.get_account_holder_name()}")
print(f"Initial Balance: ${checking_account.get_balance()}")

# Withdraw from checking account within overdraft limit
print('Withdraw from checking account within overdraft limit:')
try:
    checking_account.withdraw(500.0)
    print("Withdrawal successful of $700.0")
except OverdraftError as e:
    print(f"Error: {e}")

# Withdraw from checking account beyond overdraft limit
print('Withdraw from checking account beyond overdraft limit:')
try:
    checking_account.withdraw(1000.0)
    print("Withdrawal successful.")
except OverdraftError as e:
    print(f"Error: {e}")


# # 4. You are developing an employee management system for a company. Ensure that the system utilizes encapsulation and polymorphism to handle different types of employees, such as full-time and part-time employees.
# 
# 1. Create a base class called "Employee" with private attributes for name, employee ID, and salary. Implement getter and setter methods for these attributes.
# 
# 2. Design two subclasses, "FullTimeEmployee" and "PartTimeEmployee," that inherit from "Employee." These subclasses should encapsulate specific properties like hours worked (for part-time employees) and annual salary (for full-time employees).
# 
# 3. Override the salary calculation method in both subclasses to account for different payment structures.
# 
# 4. Write a program that demonstrates polymorphism by creating instances of both "FullTimeEmployee" and "PartTimeEmployee." Calculate their salaries and display employee information.

# In[9]:


class Employee:
    def __init__(self, name, employee_id, salary):
        self.__name = name
        self.__employee_id = employee_id
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def calculate_salary(self):
        return self.__salary

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id, annual_salary)

    def calculate_salary(self):
        return self.get_salary() / 12

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hours_worked, hourly_rate):
        super().__init__(name, employee_id, None)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

    def get_hourly_rate(self):
        return self.__hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self.__hourly_rate = hourly_rate
    
    # Calculate the salary for part-time employees
    def calculate_salary(self):
        return self.__hours_worked * self.__hourly_rate 

# Function to display employee information
def display_employee_info(employee):
    print('Name:', employee.get_name())
    print('Employee ID:', employee.get_employee_id())
    print(f"Salary: ${employee.calculate_salary():.2f}")
    print()

# Input from the user for FullTimeEmployee
full_time_name = input("Enter the name of full-time employee: ")
full_time_id = input("Enter the full-time employee's ID: ")
full_time_salary = float(input("Enter the full-time employee's annual salary: "))

# Input from the user for PartTimeEmployee
part_time_name = input("\nEnter the name of part-time employee: ")
part_time_id = input("Enter the part-time employee's ID: ")
part_time_hours_worked = float(input("Enter the part-time employee's worked hours: "))
part_time_hourly_rate = float(input("Enter the part-time employee's hourly rate: "))

# Create instances of FullTimeEmployee and PartTimeEmployee
full_time_employee = FullTimeEmployee(full_time_name, full_time_id, full_time_salary)
part_time_employee = PartTimeEmployee(part_time_name, part_time_id, part_time_hours_worked, part_time_hourly_rate)

# Display employee information using polymorphism
print("\nFull-Time Employee Information:")
display_employee_info(full_time_employee)

print("Part-Time Employee Information:")
display_employee_info(part_time_employee)


# # 5. Library Management System-Scenario: You are developing a library management system where you need to handle books, patrons, and library transactions.
# 
# 1. Create a class hierarchy that includes classes for books (e.g., Book), patrons (e.g., Patron), and transactions (e.g., Transaction). Define attributes and methods for each class.
# 
# 2. Implement encapsulation by making relevant attributes private and providing getter and setter methods where necessary.
# 
# 3. Use inheritance to represent different types of books (e.g., fiction, non-fiction) as subclasses of the Book class. Ensure that each book type can have specific attributes and methods.
# 
# 4. Demonstrate polymorphism by allowing patrons to check out and return books, regardless of the book type.
# 
# 5. Implement a method for tracking overdue books and notifying patrons.
# 
# 6. Consider scenarios like book reservations, late fees, and library staff interactions in your design.

# In[13]:


from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, publication_year, isbn, copies_available):
        self._title = title
        self._author = author
        self._publication_year = publication_year
        self._isbn = isbn
        self._copies_available = copies_available

    def get_title(self):
        return self._title

    def get_author(self):
        return self._author

    def get_publication_year(self):
        return self._publication_year

    def get_isbn(self):
        return self._isbn

    def get_copies_available(self):
        return self._copies_available

    def decrease_copies_available(self):
        if self._copies_available > 0:
            self._copies_available -= 1

    def increase_copies_available(self):
        self._copies_available += 1

    def is_available(self):
        return self._copies_available > 0

    def __str__(self):
        return f"{self._title} by {self._author} ({self._publication_year})"

class FictionBook(Book):
    def __init__(self, title, author, publication_year, isbn, copies_available, genre):
        super().__init__(title, author, publication_year, isbn, copies_available)
        self._genre = genre

    def get_genre(self):
        return self._genre

    def __str__(self):
        return super().__str__() + f", Fiction ({self._genre})"

class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, isbn, copies_available, subject):
        super().__init__(title, author, publication_year, isbn, copies_available)
        self._subject = subject

    def get_subject(self):
        return self._subject

    def __str__(self):
        return super().__str__() + f", Non-Fiction ({self._subject})"

class Patron:
    def __init__(self, patron_id, name, email):
        self._patron_id = patron_id
        self._name = name
        self._email = email
        self._checked_out_books = {}  # {Book: due_date}

    def get_patron_id(self):
        return self._patron_id

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def check_out_book(self, book, due_date):
        if book.is_available():
            book.decrease_copies_available()
            self._checked_out_books[book] = due_date
            return True
        else:
            return False

    def return_book(self, book):
        if book in self._checked_out_books:
            book.increase_copies_available()
            del self._checked_out_books[book]

    def get_checked_out_books(self):
        return self._checked_out_books

    def __str__(self):
        return f"Patron {self._patron_id}: {self._name} ({self._email})"

class Transaction:
    def __init__(self, book, patron, checkout_date, due_date):
        self._book = book
        self._patron = patron
        self._checkout_date = checkout_date
        self._due_date = due_date

    def get_book(self):
        return self._book

    def get_patron(self):
        return self._patron

    def get_checkout_date(self):
        return self._checkout_date

    def get_due_date(self):
        return self._due_date

    def is_overdue(self):
        return datetime.now() > self._due_date

    def __str__(self):
        return f"Transaction: {self._book.get_title()} checked out by {self._patron.get_name()} on {self._checkout_date}, due on {self._due_date}"

# Create books
book1 = FictionBook("Harry Potter", "J.K. Rowling", 1997, "978-0439708180", 5, "Fantasy")
book2 = NonFictionBook("Sapiens", "Yuval Noah Harari", 2014, "978-0062316097", 3, "History")

# Create patrons
patron1 = Patron(1, "John Doe", "john@example.com")
patron2 = Patron(2, "Jane Smith", "jane@example.com")

# Patrons check out books
due_date = datetime.now() + timedelta(days=14)
patron1.check_out_book(book1, due_date)
patron2.check_out_book(book2, due_date)

# Create transactions
transaction1 = Transaction(book1, patron1, datetime.now() - timedelta(days=7), due_date)
transaction2 = Transaction(book2, patron2, datetime.now() - timedelta(days=2), due_date)

# Check if transactions are overdue
if transaction1.is_overdue():
    print(f"{transaction1} is overdue.")
else:
    print(f"{transaction1} is not overdue.")

if transaction2.is_overdue():
    print(f"{transaction2} is overdue.")
else:
    print(f"{transaction2} is not overdue.")

# Patrons return books
patron1.return_book(book1)
patron2.return_book(book2)

# Check available copies of books
print(f"Available copies of {book1}: {book1.get_copies_available()}")
print(f"Available copies of {book2}: {book2.get_copies_available()}")


# # 6.Online Shopping Cart
# 
# Scenario: You are tasked with designing a class hierarchy for an online shopping cart system. The system should handle products, shopping carts, and orders. Consider various OOP principles while designing this system.
# 
# 1. Create a class hierarchy that includes classes for products (e.g., Product), shopping carts (e.g., ShoppingCart), and orders (e.g., Order). Define attributes and methods for each class.
# 
# 2. Implement encapsulation by making relevant attributes private and providing getter and setter methods where necessary.
# 
# 3. Use inheritance to represent different types of products (e.g., electronics, clothing) as subclasses of the Product class. Ensure that each product type can have specific attributes and methods.
# 
# 4. Demonstrate polymorphism by allowing various product types to be added to a shopping cart and calculate the total cost of items in the cart.
# 
# 5. Implement a method for placing an order, which transfers items from the shopping cart to an order.
# 
# Consider scenarios like out-of-stock products, discounts, and shipping costs in your design.

# In[3]:


class Product:
    def __init__(self, product_id, name, price, description, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__description = description
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_description(self):
        return self.__description

    def get_stock(self):
        return self.__stock

    def set_price(self, price):
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_stock(self, stock):
        self.__stock = stock

    def __str__(self):
        return f"{self.__name} - ${self.__price}"

class Electronics(Product):
    def __init__(self, product_id, name, price, description, stock, warranty):
        super().__init__(product_id, name, price, description, stock)
        self.__warranty = warranty

    def get_warranty(self):
        return self.__warranty

    def set_warranty(self, warranty):
        self.__warranty = warranty

    def __str__(self):
        return f"{super().__str__()} (Warranty: {self.__warranty} months)"

class Clothing(Product):
    def __init__(self, product_id, name, price, description, stock, size):
        super().__init__(product_id, name, price, description, stock)
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    def __str__(self):
        return f"{super().__str__()} (Size: {self.__size})"

class ShoppingCart:
    def __init__(self):
        self.__items = []

    def add_item(self, product, quantity):
        if (product.get_stock() >= quantity):
            self.__items.append({"product": product, "quantity": quantity})
            product.set_stock(product.get_stock() - quantity)
            return True
        else:
            return False

    def remove_item(self, product, quantity):
        for item in self.__items:
            if (item["product"] == product):
                if (item["quantity"] >= quantity):
                    item["quantity"] -= quantity
                    product.set_stock(product.get_stock() + quantity)
                    if (item["quantity"] == 0):
                        self.__items.remove(item)
                    return True
                else:
                    return False
        return False

    def calculate_total_cost(self):
        total_cost = 0
        for item in self.__items:
            total_cost += item["product"].get_price() * item["quantity"]
        return total_cost

    def view_cart(self):
        for item in self.__items:
            product, quantity = item["product"], item["quantity"]
            print(f"{product.get_name()} ({product.get_price()} x {quantity})")

class Order:
    def __init__(self, order_id, customer_name, cart):
        self.__order_id = order_id
        self.__customer_name = customer_name
        self.__cart = cart

    def place_order(self):
        # payment processing
        pass

    def get_order_summary(self):
        return f"Order ID: {self.__order_id}\nCustomer: {self.__customer_name}\nTotal Cost: ${self.__cart.calculate_total_cost()}"

# Example usage with user input:
electronics_product = Electronics(1, "Laptop", 1000, "High-performance laptop", 10, 24)
clothing_product = Clothing(2, "T-shirt", 90, "Cotton T-shirt", 50, "M")

cart = ShoppingCart()

while True:
    print("\n1. Add product to the cart")
    print("2. Remove product from cart")
    print("3. View cart")
    print("4. Checkout and place order")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Available Products:")
        print("1. Laptop - $1000")
        print("2. T-shirt - $90")
        product_choice = input("Enter the product number: ")
        quantity = int(input("Enter the quantity: "))
        if (product_choice == "1"):
            cart.add_item(electronics_product, quantity)
        elif (product_choice == "2"):
            cart.add_item(clothing_product, quantity)
        else:
            print("Invalid product choice.")

    elif choice == "2":
        cart.view_cart()
        product_choice = input("Enter the product number to remove: ")
        quantity = int(input("Enter the quantity to remove: "))
        if (product_choice == "1"):
            cart.remove_item(electronics_product, quantity)
        elif (product_choice == "2"):
            cart.remove_item(clothing_product, quantity)
        else:
            print("Invalid product choice.")

    elif choice == "3":
        print("\nShopping Cart Contents:")
        cart.view_cart()

    elif choice == "4":
        if cart.calculate_total_cost() > 0:
            customer_name = input("Enter your name: ")
            order = Order(1001, customer_name, cart)
            print("\nOrder Summary:")
            print(order.get_order_summary())
            order.place_order()
            print("Checked out & Order placed successfully!")
        else:
            print("Your cart is empty. Please add items to your cart first.")

    elif choice == "5":
        print("Thanks for shopping with us. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

