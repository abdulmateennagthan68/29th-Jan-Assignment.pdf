#!/usr/bin/env python
# coding: utf-8

# In[1]:


# who developed python programing language?


#  Guido van Rossum

# In[3]:


# which type of programing does python support


# # Procedural programming
# Object-oriented programming,
# Functional programming,
# Aspect-oriented programming,
# Concurrent programming,
# Metaprogramming,

# In[4]:


# is python is case sensitive when dealing with identifiers?


# # Yes, Python is a case-sensitive language when it comes to identifiers such as variable names, function names, class names, etc. This means that uppercase and lowercase letters are considered as different characters, and using them interchangeably can lead to errors.

# In[5]:


# what is the correct extension of the python file?


# .py

# In[7]:


# is python code compiled or interpreted?


# Yes, indentation is required in Python. Unlike many other programming languages, Python uses whitespace indentation to define the structure and hierarchy of code blocks, such as loops, conditionals, and functions.

# In[8]:


# name a few block of code used to define in python language


# if block - used to test a condition and execute code if the condition is true
# else block - used with an if block to execute code if the condition is false
# elif block - used with an if block to test additional conditions if the first condition is false
# for loop - used to iterate over a sequence of values and execute code for each value
# while loop - used to repeatedly execute code while a condition is true
# def block - used to define a function and its code block
# class block - used to define a class and its methods
# try block - used to enclose code that may raise an exception and handle the exception if it occurs
# except block - used with a try block to handle a specific exception if it occurs
# finally block - used with a try block to execute code regardless of whether an exception was raised or not.

# # Python is an interpreted language, which means that the code is executed line-by-line at runtime by an interpreter.
# Python code is compiled into bytecode, a low-level, platform-independent representation of the code, before it is executed by the interpreter

# In[9]:


# state a charater used to give single-line comments in python ?


# #  '''  for multiline '''

# In[11]:


# mention a function which helps to find the version of python that we are currently working on?


# import sys
# 
# print("Python version")
# print(sys.version)
# print("Version info.")
# print(sys.version_info)

# In[13]:


#python supports the creation of anonymous functions at a runtime,using a constructor called ----------------


# sum = lambda a, b: a + b
# print(sum(2, 3))  # Output: 5
# 

# # Python supports the creation of anonymous functions at runtime using a constructor called lambda.
# 

# In[16]:


# what does pip stands for in python?


# # pip install package_name
# 

# # pip install --upgrade package_name
# 

# # pip uninstall package_name
# 

# # pip list
# 

# # pip search search_term
# 

# In[22]:


# mention a few built -in functions in python?


# print(): This function is used to output values to the console.
# 
# len(): This function is used to get the length of a string, list, tuple, dictionary, or set.
# 
# type(): This function is used to get the type of an object.
# 
# range(): This function is used to generate a sequence of numbers.
# 
# int(), float(), str(), bool(): These functions are used to convert values from one data type to another.
# 
# input(): This function is used to get user input from the console.
# 
# sum(): This function is used to get the sum of a list of numbers.
# 
# max(), min(): These functions are used to get the maximum and minimum values in a list of numbers.
# 
# abs(): This function is used to get the absolute value of a number.
# 
# sorted(): This function is used to sort a list or other iterable.

# In[23]:


# what is the maximum possible length of an identifier in python


# In Python, the maximum possible length of an identifier is not explicitly defined. However, it is recommended to keep the length of an identifier under 79 characters, as per the PEP 8 style guide.

# In[24]:


# what are the benifits of using python?


# Easy to learn: Python has a simple and easy-to-understand syntax that makes it easy to learn, even for beginners.
# 
# Large community and resources: Python has a large and active community of developers, which means that there are many resources available online, including documentation, tutorials, and libraries.
# 
# Versatile: Python can be used for a wide range of applications, including web development, scientific computing, data analysis, artificial intelligence, and more.
# 
# Cross-platform: Python is a cross-platform language, meaning that code written on one platform can run on other platforms without modification.
# 
# Readability: Python has a clear and concise syntax that makes code easy to read and understand, even for those who are not familiar with the language.
# 
# Productivity: Python has a large number of third-party libraries and tools that can help developers be more productive, such as NumPy, Pandas, and Django.
# 
# Scalability: Python is highly scalable, which means that it can be used to build small scripts as well as large-scale applications.
# 
# Integration: Python can easily be integrated with other languages and technologies, making it a great choice for building complex systems.

# In[25]:


# how is memory management in python?


# Memory management in Python is handled automatically by the built-in memory manager.
# Python uses a technique called garbage collection to automatically free up memory that is no longer being used.
# The memory manager is responsible for allocating and deallocating memory for objects in the program.
# Python uses reference counting to keep track of the number of references to an object and frees up memory when an object's reference count drops to zero.
# Python also uses cyclic garbage collection to handle objects that reference each other in a cycle.
# Overall, Python's memory management system is designed to be efficient and automatic, freeing developers from the need to manually manage memory in their programs.

# In[26]:


# how to install python on windows and set  path variable?


# Go to the official Python website at https://www.python.org/downloads/ and download the latest version of Python for Windows.
# 
# Run the installer and follow the on-screen instructions to install Python on your computer. Make sure to select the option to add Python to the PATH variable during the installation process.
# 
# Once the installation is complete, open the command prompt by pressing the Windows key + R and typing "cmd" in the Run dialog box.
# 
# Type "python" in the command prompt and press Enter to check if Python is installed correctly. If you see a message that says "Python X.X.X", where X.X.X is the version number, then Python is installed correctly.
# 
# If you get an error message, you may need to add the Python installation directory to the PATH variable manually. To do this, go to Control Panel > System and Security > System > Advanced system settings > Environment Variables.
# 
# In the Environment Variables window, scroll down to the System Variables section and find the "Path" variable. Click on "Edit" to open the Edit Environment Variable dialog box.
# 
# Click on "New" and add the path to the Python installation directory. The default installation path is "C:\PythonXX", where XX is the version number.
# 
# Click on "OK" to save the changes and close all the windows.
# 
# Open a new command prompt and type "python" again to check if Python is now installed and set up correctly.
# 
# That's it! You have successfully installed Python on Windows and set the PATH variable.

# In[27]:


# is indentation required in python?


# Yes, indentation is required in Python. Unlike many other programming languages, Python uses whitespace indentation to define the structure and hierarchy of code blocks, such as loops, conditionals, and functions.
