#!/usr/bin/env python
# coding: utf-8

# # MODULES AND VIRTUAL ENVIRONMENTS

# # 1. Module Import and Management
# 
# Scenario: You are developing a complex Python project with multiple modules. To manage the project effectively, you need to import and use various modules. Additionally, you want to organize your code using namespaces and avoid naming conflicts.
# 
# Design a Python program that demonstrates the following:
# 
# 1. Import multiple modules within your project.
# 
# 2. Use the import statement to access functions, classes, and variables from imported modules.
# 
# 3. Create your custom module and use it in your main program.
# 
# 4. Handle naming conflicts and ensure proper namespacing.
# 
# 5. Implement error handling for missing modules or incorrect module usage.

# In[1]:


# custom_module.py
def greet(name):
        return 'Hello ' + name


# In[6]:


# importing custome module
from custom_module import greet

try:
    # 1. Import multiple modules within your project.
    import math
    import calendar
    import datetime
    
    # 2. Use the import statement to access functions, classes, and variables from imported modules.
    n = int(input('\nEnter the value of n: '))  
    print('Using the math module:')
    print('The square root of', n,'is', math.sqrt(n))
    print('The factorial of', n,'is', math.factorial(n))
    
    print('\nUsing the calendar module:')
    year = int(input('\nEnter the year: '))
    print('The calendar for', year,'is:\n', calendar.calendar(year))
    
    print('\nUsing the datetime module:')
    print('The current date is:', datetime.date.today()) 
    
    # 3. Create your custom module and use it in your main program.
    print('\nUsing the custom module:')
    name = input('Enter name:')
    print('Greetings:', greet(name))
      
    # 4. Handle naming conflicts and ensure proper namespacing.
    print('\nThe current date:',datetime.date.today())
    print('After handling name conflicts and ensure proper namespacing,')
    today = datetime.date.today()
    print('The current date:','[',today,']')
    
    # 5. Implement error handling for missing modules or incorrect module usage.
except ModuleNotFoundError as e:
    print(print('Error:',e,' \n Module not found'))
except AttributeError as e:
    print('Error:',e,'\n Attribute not found in the module')
except Exception as e:
    print('Error:',e)


# # 2. Virtual Environment Management
# 
# Scenario: You are working on multiple Python projects with different dependencies and versions. To avoid conflicts and ensure project isolation, you decide to use virtual environments.
# 
# Create a Python program that demonstrates the following: 
# 
# 1. Create a virtual environment for a specific project.
# 
# 2. Activate and deactivate virtual environments.
# 
# 1. Install, upgrade, and uninstall packages within a virtual environment.
# 
# 4. List the installed packages in a virtual environment.
# 
# 5. Implement error handling for virtual environment operations.

# In[8]:


import subprocess
import os
import sys

def create_virtual_environment(venv_name):
    try:
        subprocess.run(['python', '-m', 'venv', venv_name], check = True)
        print('The virtual environment {} is created successfully.'.format(venv_name))
    except subprocess.CalledProcessError as e:
        print('Error in creating virtual environment {}: {}'.format(venv_name, e))
        sys.exit(1)

def activate_virtual_environment(venv_name):
    venv_path = os.path.abspath(venv_name)
    activate_script = os.path.join(venv_path, 'Scripts' if os.name == 'nt' else 'bin', 'activate')
    try:
        subprocess.run([activate_script], shell = True, check = True)
        print('Activated the virtual environment {}.'.format(venv_name))
    except subprocess.CalledProcessError as e:
        print('Error in activating virtual environment {}: {}'.format(venv_name, e))
        sys.exit(1)

def deactivate_virtual_environment(venv_name):
    try:
        subprocess.run(['deactivate'], shell = True, check = True)
        print('Deactivated the virtual environment {}.'.format(venv_name))
    except subprocess.CalledProcessError as e:
        print('Error in deactivating virtual environment {}: {}'.format(venv_name, e))
        sys.exit(1)

def install_package(package_name):
    try:
        subprocess.run(['pip', 'install', package_name], check = True)
        print('Package ',package_name,' is installed successfully.')
    except subprocess.CalledProcessError as e:
        print('Error in installing package ', package_name,':', e)
        sys.exit(1)

def upgrade_package(package_name):
    try:
        subprocess.run(['pip', 'install', '--upgrade', package_name], check = True)
        print('Package ',package_name,' is upgraded successfully.')
    except subprocess.CalledProcessError as e:
        print('Error in upgrading package ', package_name,':', e)
        sys.exit(1)

def uninstall_package(package_name):
    try:
        subprocess.run(['pip', 'uninstall', package_name, '-y'], check = True)
        print('Package ',package_name,' is uninstalled successfully.')
    except subprocess.CalledProcessError as e:
        print('Error in uninstalling package ', package_name,':', e)
        sys.exit(1)

def list_installed_packages():
    try:
         #subprocess.run(['pip', 'list'], check = True)
        result = subprocess.run(['pip', 'list'], capture_output = True, text = True, check = True)
        installed_packages = result.stdout

        # Print the list of installed packages
        print('List of installed packages in the virtual environment:')
        print(installed_packages)
    except subprocess.CalledProcessError as e:
        print('Error listing installed packages:', e)
        
# Define the name of your virtual environment
venv_name = 'chandu_virtual_env'

# Create a virtual environment
create_virtual_environment(venv_name)

# Activate the virtual environment
activate_virtual_environment(venv_name)

# Install, upgrade, or uninstall packages within the virtual environment
install_package('numpy')
upgrade_package('numpy')
uninstall_package('numpy')

# List installed packages in the virtual environment
list_installed_packages()

# Deactivate the virtual environment
deactivate_virtual_environment(venv_name)


# # 3. Module Dependency Resolution
# 
# Scenario: You are developing a Python application that relies on third-party packages. Managing dependencies and ensuring compatibility is crucial for your project's success.
# 
# Design a Python program that demonstrates the following: 
# 
# 1. Use a requirements.txt file to specify project dependencies.
# 
# 2. Automatically install all project dependencies from the requirements.txt file.
# 
# 3. Ensure that the versions of installed packages are compatible.
# 
# 4. Implement error handling for dependency resolution and installation.

# In[9]:


import subprocess
import sys

def install_dependencies():
    try:
        # Use subprocess to run 'pip install -r requirements.txt'
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print('The Dependencies were installed successfully.\nAlso, the versions of installed packages are compatible.')
    
    except subprocess.CalledProcessError as e:
        print('Error installing dependencies:', e)
    except FileNotFoundError:
        print('pip is not installed. Please install pip and try again.')

try:
    # Read the requirements.txt file
    with open('requirements.txt', 'r') as requirements_file:
        requirements = requirements_file.read().splitlines()

     # Install dependencies
    install_dependencies()
except FileNotFoundError:
    print("requirements.txt file not found. Please create one with your project's dependencies.")
except Exception as e:
    print('An error occurred:', e)


# # DATABASE PROGRAMMING WITH MYSQL

# # 1. Implement Inventory Management in Python with MySQL
# 
# a) Inventory management, a critical element of the supply chain, is the tracking of inventory from manufacturers to warehouses and from these facilities to a point of sale. The goal of inventory management is to have the right products in the right place at the right time.
# 
# b) The required Database is Inventory, and the required Tables are Purchases, Sales and Inventory
# 
# c) Note: Apply your thoughts to demonstrate the DB Operation in Python.

# In[20]:


import mysql.connector

try:
    my_db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Chandana@2631",
    database="inventory"
     )
    cursor = my_db.cursor()

    # Create the Purchases table
    cursor.execute("CREATE TABLE IF NOT EXISTS Purchases (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, product_id INT NOT NULL," 
                   "quantity INT NOT NULL, purchase_date DATE NOT NULL)")

    # Create the Sales table
    cursor.execute("CREATE TABLE IF NOT EXISTS Sales (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT NOT NULL,"
                   "quantity INT NOT NULL, sale_date DATE NOT NULL)")

    # Create the Inventory table
    cursor.execute("CREATE TABLE IF NOT EXISTS Inventory (id INT AUTO_INCREMENT PRIMARY KEY, product_id INT NOT NULL,"
                   "quantity INT NOT NULL)")

    # Insert a purchase record
    cursor.execute('INSERT INTO Purchases (product_id, quantity, purchase_date) VALUES (1, 8, NOW())')

    # Update the inventory quantity
    cursor.execute('UPDATE Inventory SET quantity = quantity + 5 WHERE product_id = 1')
    print('The products were purchased successfully!')

    # Insert a sales record
    cursor.execute('INSERT INTO Sales (product_id, quantity, sale_date) VALUES (1, 10, NOW())')

    # Update the inventory quantity
    cursor.execute('UPDATE Inventory SET quantity = quantity - 2 WHERE product_id = 1')
    print('The products were sold successfully!')

    my_db.commit()
    cursor.close()
    my_db.close()
except Exception as e:
    print(e)  


# # 2. Customer Order Processing
# 
# Scenario: You are building a customer order processing system for an e-commerce company. The system needs to interact with a MySQL database to store customer orders, products, and order details.
# 
# 1. Design a MySQL database schema for the order processing system, including tables for customers, products, and orders.
# 
# 2. Write a Python program that connects to the database and allows customers to place new orders.
# 
# 3. Implement a feature that calculates the total cost of an order and updates product quantities in the database.
# 
# 4. How would you handle cases where a product is no longer available when a customer places an order?
# 
# 5. Develop a function to generate order reports for the company's finance department.

# In[10]:


import mysql.connector

# Connect to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Chandana@2631",
        database="order_processing_system"
        )
        return conn
    except mysql.connector.Error as err:
        print('Error:', err)
        return None

# Function to place a new order
def place_order(customer_id, product_id, quantity):
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor()

            # Check if the product is available
            cursor.execute("SELECT quantity_available, price FROM Products WHERE product_id = %s", (product_id,))
            product_info = cursor.fetchone()

            if product_info and product_info[0] >= quantity:
                unit_price = product_info[1]
                line_total = unit_price * quantity

                # Insert the order into the Orders table
                cursor.execute("INSERT INTO Orders (customer_id, order_date, order_status, total_amount) VALUES (%s, %s, %s, %s)", (customer_id, "2023-09-16 12:00:00", "received", line_total))
                order_id = cursor.lastrowid

                # Insert the order details into the OrderDetails table
                cursor.execute("INSERT INTO OrderDetails (order_id, product_id, quantity_ordered, unit_price, line_total_amount) VALUES (%s, %s, %s, %s, %s)",
                               (order_id, product_id, quantity, unit_price, line_total))

                # Update product quantity
                new_quantity = product_info[0] - quantity
                cursor.execute("UPDATE Products SET quantity_available = %s WHERE product_id = %s", (new_quantity, product_id))

                conn.commit()
                print("Order placed successfully!")
            else:
                print("Product is out of stock or quantity is insufficient.")

        except mysql.connector.Error as err:
            print('Error:', err)
        finally:
            cursor.close()
            conn.close()

# Function to generate order reports
def generate_order_report():
    conn = connect_to_database()
    if conn:
        try:
            cursor = conn.cursor(dictionary = True)

            # Fetch order details for reporting
            cursor.execute("SELECT O.order_id, C.name AS customer_name, P.name AS product_name, OD.quantity_ordered, OD.unit_price, OD.line_total_amount, O.order_date FROM Orders O "
                           "JOIN Customers C ON O.customer_id = C.customer_id "
                           "JOIN OrderDetails OD ON O.order_id = OD.order_id "
                           "JOIN Products P ON OD.product_id = P.product_id")
            
            orders = cursor.fetchall()

            if orders:
                print("\nOrder Report generated:")
                for order in orders:
                    print(f"Order ID: {order['order_id']}")
                    print(f"Customer Name: {order['customer_name']}")
                    print(f"Product Name: {order['product_name']}")
                    print(f"Quantity Ordered: {order['quantity_ordered']}")
                    print(f"Unit Price: ${order['unit_price']:.2f}")
                    print(f"Line Total: ${order['line_total_amount']:.2f}")
                    print(f"Order Date: {order['order_date']}")
                    print("\n")
            else:
                print("No orders found.")

        except mysql.connector.Error as err:
            print('Error:', err)
        finally:
            cursor.close()
            conn.close()

customer_id = int(input('Enter the customer_id : '))
product_id = int(input('Enter the product_id : '))
quantity = int(input('Enter the quantity : '))
place_order(customer_id, product_id, quantity)
generate_order_report()


# # 3. You are tasked with developing a Python program that connects to a MySQL database, retrieves data from a table, performs some operations on the data, and updates the database with the modified data. Please write Python code to accomplish this task.
# 
# Instructions:
# 
# 1. Assume that you have a MySQL database server running with the following details:
# 
#    i)    Host: localhost
#    
#    ii)   Port: 3306
# 
#    iii)  Username: your_username
#    
#    iv)   Password: your_password
# 
#    v)    Database Name: your_database
# 
#    vi)   Table Name: your_table 
#    
#    vii)  The table has the following columns: id (int), name (varchar), quantity (int).
# 
# 2. Your Python program should:
# 
#    i)    Connect to the MySQL database.
# 
#    ii)   Retrieve all records from the your_table table. 
#    
#    iii)  Calculate the total quantity of all records retrieved.
# 
#    iv)   Update the quantity column of each record by doubling its value.
# 
#    v)    Commit the changes to the database. 
#    
#    vi)   Close the database connection.
# 
# 3. Handle any potential errors that may occur during the database connection and data manipulation, such as connection failures or SQL errors
# 
# 4. Provide comments in your code to explain each step.

# In[10]:


#Importing MYSQLConnector to connect python with the database 
import mysql.connector

# Handling the errors using try block
try:
    # Connecting to the MySQL database by giving connection details
    my_db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Chandana@2631",
        database="day5"  # Accessing the database 'day5' for performing operations on data 
    )
    # Checking whether the connection is successful or not
    if my_db.is_connected():
        print("Connected to MySQL database")

        # Creating a cursor object to interact with the database
        cursor = my_db.cursor()

        # Retrieving all records from the 'new_table' table
        cursor.execute("SELECT * FROM new_table")
        records = cursor.fetchall()
        # Calculating the total quantity of all records that are retrieved before and printing it
        total_quantity = sum(record[2] for record in records)
        print('Total quantity at intial stage:', total_quantity)

        # Doubling the quantity for each record and updating the database
        double_count = 0
        for record in records:
            new_quantity = record[2] * 2
            double_count = new_quantity + double_count
            cursor.execute("UPDATE new_table SET quantity = %s WHERE id = %s", (new_quantity, record[0]))
        print('Total quantity after doubling:', double_count)
        # Commiting the changes to the database
        my_db.commit()
        print("Therefore, changes are committed to the database.")

# Handling potential errors using except block 
except mysql.connector.Error as err:
    print('Error:', err)

# Closing the cursor and database using finaly block    
finally:
    if my_db.is_connected():
        cursor.close()
        my_db.close()
        print("The Database connection is closed")


# # 4. You are developing an employee management system for a company. The database should store employee information, including name, salary, department, and hire date. Managers should be able to view and update employee details.
# 
# 1. Design the database schema for the employee management system.
# 
# 2. Write Python code to connect to the database and retrieve a list of employees in a specific department.
# 
# 3. Implement a feature to update an employee's salary.

# In[11]:


import mysql.connector

def connect_to_db():
    db = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="Chandana@2631",
        database="employee_management_system"
        )
    return db

def get_employees_by_department(department):
    
    # Retrieving a list of employees in a specific department.
    db = connect_to_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM employees WHERE department = %s', (department,))
    employees = cursor.fetchall()

    # Convert the employee records to dictionaries.
    employee_dicts = []
    for employee in employees:
        employee_dict = {
            'employee_id': employee[0],
            'name': employee[1],
            'salary': employee[2],
            'department': employee[3],
            'hire_date': employee[4]
    }
    employee_dicts.append(employee_dict)

    # Close the database connection.
    db.close()

    return employee_dicts

def update_employee_salary(employee_id, new_salary):
    
    # Updates an employee's salary.
    db = connect_to_db()
    cursor = db.cursor()

    cursor.execute('UPDATE employees SET salary = %s WHERE employee_id = %s', (new_salary, employee_id))
    db.commit()

    # Close the database connection.
    db.close()
    
# Get the department name from the user.
department = input('Enter department name: ')

# Retrieve a list of employees in the specified department.
employees = get_employees_by_department(department)

# Print the list of employees to the console.
for employee in employees:
    print(employee['name'])
        
# Get the employee ID and new salary from the user.
print('Enter the employee details to update their salary')
employee_id = int(input('Enter employee ID: '))
new_salary = float(input('Enter new salary: '))

# Update the employee's salary.
update_employee_salary(employee_id, new_salary)
print('Employee salary was updated successfully!')

