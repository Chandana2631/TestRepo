#!/usr/bin/env python
# coding: utf-8

# # FILE HANDLING

# # 1. Write a python function that copies a file reading and writing up to 50 characters at a time.

# In[50]:


def copy_file_upto_50_characters():
    file = open('AI.txt','r')
    copy_file = open('AI_copy_file.txt','w')
    txt = file.read(50)
    print(txt)
    copy_file.write(txt)

    file.close()
    copy_file.close()

copy_file_upto_50_characters()


# # 2. Print all numbers present in the text file and print the number of blank spaces in that file.
# 

# In[49]:


file = open('let_num.txt','r')
num_count = 0
spaces_count = 0
print('\nThe numbers present in the file are :',end = ' ')
for line in file:
    for char in line:
        if char.isdigit():
            print(char, end=' ')
            num_count = num_count + 1
        elif char.isspace():
            spaces_count = spaces_count + 1
print('\n\nThe total number of blank spaces present in the file is :', spaces_count)
file.close()


# # 3. Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string. If an error occurs while opening, reading, writing, or closing files, your program should catch the exception, print an error message, and exit.

# In[27]:


def sed(pattern_string, replacement_string, first_file, second_file):
    try:
        first_file = open('let_num.txt','r')
        contents = first_file.read()
        print(contents)
        print('\nNew file is:\n')
        second_file = open('sed.txt','w')
        second_file.write(contents.replace(pattern_string, replacement_string))
        second_file = open('sed.txt','r')
        new_file = second_file.read()
        print(new_file)
        first_file.close()
        second_file.close()
        
    except FileNotFoundError as e:
        print('Error')
        exit(1)
    except Exception as e:
        print('Error')
        exit(1)
pattern_string = 'mphasis'
replacement_string = 'mphasis limited'
print('\nOld file is:\n')
sed(pattern_string, replacement_string, first_file, second_file)


# # 4. Log File Analysis: You have a log file containing records of user activities on a website. Each line in the file represents a log entry with details like timestamp, user ID, and action performed. Your task is to analyze this log file.
# 
#    a. Write Python code to read the log file and extract specific information, such as the number of unique users or the most common action.
# 
#    b. How would you handle large log files efficiently without loading the entire file into memory?

# In[5]:


def parse_log_file(log_file_path):
    log_entries_by_date = {}
    with open(log_file_path,'r') as log_file:
        for line in log_file:
            parts = line.strip().split(' ',1)
            if len(parts) == 2:
                timestamp,message = parts
                date = timestamp[:10]
                if date in log_entries_by_date:
                    log_entries_by_date[date].append(message)
                else:
                    log_entries_by_date[date] = [message]
    return log_entries_by_date

def analyze_log_data(log_entries_by_date):
    for date, entries in log_entries_by_date.items():
        print(f"Date: {date}")
        print(f"Total Entries: {len(entries)}")
        print("Sample Entries:")
        for i, entry in enumerate(entries[:5],start=1):
            print(f"{i}. {entry}")
        print("---------")
        
log_file_path = "logfile.txt"
log_entries_by_date = parse_log_file(log_file_path)
analyze_log_data(log_entries_by_date)      


# # 5. Text File Search and Replace: You have a text file with a large amount of text, and you want to search for specific words or phrases and replace them with new content.

# # a. Write Python code to search for and replace text within a text file.

# In[59]:


def search_and_replace(file, text_or_phrase, replace_with):
    try:
        with open(file, 'r') as read_file:
            content = read_file.read()
        updated_content = content.replace(text_or_phrase, replace_with)
        with open(file, 'w') as write_file:
            write_file.write(updated_content)
        print('\nSearch and replace was completed successfully in', file)
        
    except FileNotFoundError:
        print('File is not found')
    except Exception as e:
        print(e,'Error')

file = 'AI.txt'
text_or_phrase = 'complex tasks'
replace_with = 'difficult tasks'
search_and_replace(file, text_or_phrase, replace_with)


# # b. How would you handle cases where you need to perform multiple replacements in a single pass?

# In[60]:


def search_and_replace(file, replacements):
    try:
        with open(file, 'r') as read_file:
            content = read_file.read()

        for search_text, replace_text in replacements:
            content = content.replace(search_text, replace_text)

        with open(file, 'w') as write_file:
            write_file.write(content)
        print('\nSearch and replace of multiple replacements in a single pass was completed successfully in', file)

    except FileNotFoundError:
        print('File is not found')
    except Exception as e:
        print('Error:', e)

file = 'AI.txt'
replacements = [('many', 'large'),('difficult', 'complex'),('and', '&')]

search_and_replace(file, replacements)


# # 6. Write a Python script that concatenates the contents of multiple text files into a single output file. Allow the user to specify the input files and the output file.

# In[45]:


def concat_files(input_files, output_file):
    with open(output_file, 'w') as output_file:
        for input_file in input_files:
            with open(input_file, "r") as input_file:
                output_file.write(input_file.read())
        print('\nAll input files are concatenated and are stored in output file')
        
inp_files = []
while True:
    inp_file = input('\nEnter the input text file to concatenate or press enter if there are not any : ')
    if inp_file == '':
        break
    inp_files.append(inp_file)
output_file = input('\nEnter the output text file to store the output: ')

concat_files(inp_files, output_file)


# # 7. You are given a text file named input.txt containing a list of words, one                word per line. Your task is to create a Python program that reads the                    contents of input.txt, processes the words, and writes the result to an                  output file named output.txt.The program should perform the following                operations:
# 
#        Note: Your code should work for any input file containing words and produce the corresponding word-length dictionary in the output file.

# # i.   Read the words from input.txt.

# In[76]:


try:
    print('\nThe words that are read from input.txt file are :')
    with open('input.txt','r') as input_file:
        content=input_file.read()
        print(content)
        print()
finally:
    input_file.close()


# # ii.  For each word in the input file, calculate the length of the word and store it         in a dictionary where the word is the key, and the length is the value.
# 

# In[110]:


word_length_dict = {}
try:
    with open('input.txt','r') as input_file:
        for line in input_file:
            word = line.strip() 
            word_length = len(word) 
            word_length_dict[word] = word_length 
    print('\nA dictionary is created with word as key and length as value')

except FileNotFoundError:
    print('File is not found')
except Exception as e:
    print('Error:', e)


# # iii. Write the word-length dictionary to output.txt in the following format:
# 
#          Word1: Length1
#          Word2: Length2
#          ---

# In[109]:


file = 'output.txt'
with open(file, 'w') as output_file:
    for word, length in word_length_dict.items():
        output_file.write('{}: {}\n'.format(word, length))
print('\nWord-length dictionary is copied to output.txt')        


# # iv.  Close both input and output files properly.
# 

# In[107]:


input_file = open('input.txt','r')
output_file = open('output.txt','r')
input_file.close()
output_file.close()
print('\nBoth input and output files are closed properly')


# # v.   Write Python code to accomplish this task. Ensure proper error handling            for file operations.
#    
#          Sample Input('input.txt')
#         
#          apple
#          banana
#          cherry
#          date
#         
#          Sample Output("output.txt')
#          
#          apple: 5
#          banana: 6
#          cherry: 6
#          date: 4

# In[108]:


file = 'output.txt'
try:
    print('\nWord-length dictionary is copied to output.txt as follows:\n')
    with open(file, 'w') as output_file:
        for word, length in word_length_dict.items():
            output_file.write('{}: {}\n'.format(word, length))
    file = open('output.txt','r')        
    content = file.read()
    print(content)

except FileNotFoundError:
    print('File is not found')
except Exception as e:
    print('Error:', e)


# # 8. Assume that you are developing a student gradebook system for a school. The system should allow teachers to input student grades for various subjects, store the data in files, and provide students with the ability to view their grades.
# 
#    Design a Python program that accomplishes the following tasks:
# 
#      i.   Teachers should be able to input grades for students in different subjects.
# 
#      ii.  Store the student grade data in separate text files for each subject.
# 
#      iii. Students should be able to view their grades for each subject.
# 
#      iv.  Implement error handling for file operations, such as file not found or permission issues.

# In[111]:


import os

# Function to input and store student grades for a subject
def input_grades(subject):
    try:
        file_name = f"{subject}.txt"
        with open(file_name, "a") as file:
            student_name = input("Enter student name: ")
            grade = input(f"Enter {subject} grade for {student_name}: ")
            file.write(f"{student_name}: {grade}\n")
        print(f"Grade for {student_name} in {subject} has been recorded.")
    except IOError as e:
        print(f"Error: {e}")

# Function to view student grades for a subject
def view_grades(subject):
    try:
        file_name = f"{subject}.txt"
        if not os.path.exists(file_name):
            print(f"No grades recorded for {subject} yet.")
            return

        with open(file_name, "r") as file:
            print(f"Grades for {subject}:")
            for line in file:
                print(line.strip())
    except IOError as e:
        print(f"Error: {e}")

# Main program loop
while True:
    print("\nStudent Gradebook System")
    print("1. Input Grades")
    print("2. View Grades")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        subject = input("Enter the subject: ")
        input_grades(subject)
    elif choice == "2":
        subject = input("Enter the subject: ")
        view_grades(subject)
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

print("Goodbye!")

