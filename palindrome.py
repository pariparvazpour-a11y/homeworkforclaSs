#!/usr/bin/env python
# coding: utf-8

# In[2]:


# code for check if input is a palindrome (string or number)

def is_palindrome(input_str):
   

    cleaned = input_str.lower().replace(" ", "")  # Ignor
    return cleaned == cleaned[::-1]

# Get input from user
user_input = input("Enter a string or number to check if it's a palindrome: ")

# Check and display result
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")

