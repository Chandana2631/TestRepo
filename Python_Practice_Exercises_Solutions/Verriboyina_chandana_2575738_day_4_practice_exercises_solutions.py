#!/usr/bin/env python
# coding: utf-8

# # EXCEPTIONS AND COMMAND-LINE ARGUMENTS

# # 1. Write a python program with Exception handling to input marks for five subjects Physics, Chemistry, Biology, Mathematics, and Computer. Calculate the percentage and grade according to the following:
# 
#    i)    Percentage >= 90%: Grade A
# 
#    ii)   Percentage >= 80% : Grade B
# 
#    iii)  Percentage>= 70% : Grade C
# 
#    iv)   Percentage >= 60% : Grade D
# 
#    v)    Percentage >= 40%: Grade E
# 
#    vi)   Percentage<40%: Grade F

# In[6]:


def Grade_fun(Percentage):
    if (Percentage >= 90):
        return 'A'
    elif (Percentage >= 80):
        return 'B'
    elif (Percentage >= 70):
        return 'C'
    elif (Percentage >= 60):
        return 'D'
    elif (Percentage >= 40):
        return 'E'
    else:
        return 'F'

try:
    mark_list = []
    subjects = ['Physics', 'Chemistry', 'Biology', 'Mathematics', 'Computer']
    for i in subjects:
        marks = float(input('Enter {} marks : '.format(i)))
        if (marks < 0) or marks > 100:
            raise ValueError('\nMarks must lie between 0 to 100.')
        mark_list.append(marks)
        
    Percentage = sum(mark_list) / 5.0
    Grade = Grade_fun(Percentage)
    print('Total percentage :', Percentage, '%')
    print('Grade :', Grade)

except ValueError as e:
    print('Error:',e,'\nSo, please enter valid marks between 0 and 100')
except Exception as e:
    print('Error:',e)


# # 2. Write a python program with Exception handling to input electricity unit charges and calculate the total electricity bill according to the given condition:
# 
#    i)    For the first 50 units Rs.0.50/unit
# 
#    ii)   For the next 100 units Rs.0.75/unit
# 
#    iii)  For the next 100 units Rs.1.20/unit
# 
#    iv)   For units above 250 Rs.1.50/unit
# 
#    v)    An additional surcharge of 20% is added to the bill.

# In[10]:


try:
    e_unit = float(input('\nEnter your electricity unit charges : '))
    if (e_unit < 0):
        raise ValueError('The electricity units cannot be negative.')
    if (e_unit<= 50):
        bill = e_unit * 0.50
    elif (e_unit <= 150):
        bill = (50 * 0.50) + ((e_unit - 50) * 0.75)
    elif (e_unit <= 250):
        bill = (50 * 0.50) + (100 * 0.75) + ((e_unit - 150) * 1.20)
    else:
        bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((e_unit - 250) * 1.50)
    surcharge = (0.20 * bill)
    total_bill = bill + surcharge
    print('\nThe total electricity bill is : Rs.', total_bill, '/-')

except ValueError as e:
    print('Error:',e,' \nSo, please enter a positive number for unit charges')
except Exception as e:
    print('Error:',e)


# # 3. Write a python program with Exception handling to input the week number and print the weekday.

# In[17]:


try:
    week_num = int(input('\nEnter the week number : '))
    if (week_num<1) or (week_num>7):
        raise ValueError('The week number must be between 1 and 7.')
    if (week_num == 1):
        week_day = 'Monday'
    elif (week_num == 2):
        week_day = 'Tuesday'
    elif (week_num == 3):
        week_day = 'Wednesday'
    elif (week_num == 4):
        week_day = 'Thursday'
    elif (week_num == 5):
        week_day = 'Friday'
    elif (week_num == 6):
        week_day = 'Saturday'
    else:
        week_day = 'Sunday'    
    print('\nThe week day for the week number {} is : {}'.format(week_num, week_day))
    
except ValueError as e:
    print('Error:', e, '\nSo, enter a valid week number between 1 and 7')
except Exception as e:
    print('Error:',e)    


# # 4. Write a Python program to implement word count using command line arguments.
# 
#    i)    Create a text document "apple.txt" which contains text for wordcount.
# 
#    ii)   Create a wordcount program which calls the "apple.txt" document by opening the file.
# 
#    iii)  If the word is present again in the "apple.txt",the wordcount is incremented by 1 until all the words are counted in the document.
# 
#    iv)   Close the file.
# 
#    v)    Create a command.py program which imports the wordcount.py program.
# 
#    vi)   Count the number of words using command line arguments.
# 
#    vii)  Print each word and its count.

# In[ ]:


#wordcount.py

import sys

def word_count(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.lower().split()
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        return word_counts

    except FileNotFoundError:
        print('Error: File not found.')
    except Exception as e:
        print('Error:',e)    
        
if len(sys.argv) != 2:
    print('Usage: python wordcount.py apple.txt')
else:
    file_name = sys.argv[1]
    word_counts = word_count(file_name)


# In[ ]:


#command.py

import sys
from wordcount import word_count

if len(sys.argv) != 2:
    print('Usage: python command.py apple.txt')
else:
    file_name = sys.argv[1]
    word_counts = word_count(file_name)

    for word, count in word_counts.items():
        print('{}: {}'.format(word,count))


# # 5. Write a Python program for finding the most frequent words in a text read from a file.
# 
# i) Initially open the text file in read mode.
# 
# ii) Make all the letters in the document into lowercase letters and split the words in each line.
# 
# iii) Get the words in an order.
# 
# iv) Sort the words for finding the most frequent words in the file.
# 
# v) Print the most frequent words in the file.

# In[28]:


# i) Initially open the text file in read mode.
try:
    file_path = input('\nEnter the name of the text file: ')
    print('\nThe content of the file is:\n')
    with open(file_path, 'r') as file:
        text = file.read()
        print(text)
        
    # ii) Make all the letters in the document into lowercase letters and split the words in each line.
    words = text.lower().split()

    # iii) Get the words in an order.
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # iv) Sort the words for finding the most frequent words in the file.
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse = True)

    # v) Print the most frequent words in the file.
    print('\nMost frequent words in the file are :\n')
    for word, count in sorted_words:
        if (count == 1):
            print('{} : {} time'.format(word,count))
        else:
            print('{} : {} times'.format(word,count))

except FileNotFoundError:
    print('Error: File not found.')
except Exception as e:
    print('Error:',e)


# # 6. File Processing with Command-Line Arguments- Scenario: You are developing a command-line utility that processes text files. Users can specify input and output file paths as command-line arguments. Your program should handle exceptions gracefully.
# 
#    i)   Design a Python program that takes two command-line arguments: the input file path and the output file path. Ensure that the program checks if both arguments are provided and that the input file exists.
# 
#    ii)  Implement error handling to deal with scenarios such as missing input files, invalid file paths, or permission issues when writing to the output file.
# 
#    iii) If an error occurs during file processing, display a user-friendly error message, and exit the program with a non-zero exit code.
# 
#    iv)  Write test cases that cover various scenarios, including providing valid and invalid file paths as command-line arguments.

# In[ ]:


import sys

def processing_files(input_file_path, output_file_path):
    try:
        # Checking whether both input & output file paths are provided or not
        if not input_file_path or not output_file_path:
            raise ValueError('Both input and output file paths are required.')
        with open(input_file_path, 'r') as input_file:
            content = input_file.read()

        # For processing, let's capitalize the first letter of every word in the file 
        processed_content = content.title()
        with open(output_file_path, 'w') as output_file:
            output_file.write(processed_content)
        print('The file processing of capitalizing the first letter of every word in the file has completed successfully.')

    except FileNotFoundError:
        print('Error: Input file is not found.')
        sys.exit(1)  # Exiting the program with a non-zero exit code
    except PermissionError:
        print('Error: Permission is denied while writing to the output file.')
        sys.exit(1)
    except Exception as e:
        print('Error:',e)
        sys.exit(1)

# Checking if two command-line arguments are provided (input and output file paths) & the other one is python program file
if len(sys.argv) != 3:
    print('Usage: python program.py input_file.txt output_file.txt')
    sys.exit(1)
input_file_path = sys.argv[1]
output_file_path = sys.argv[2]

processing_files(input_file_path, output_file_path)

