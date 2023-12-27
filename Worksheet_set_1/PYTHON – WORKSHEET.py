#!/usr/bin/env python
# coding: utf-8

# 1) %

# 2) 0

# 3) 24

# 4) 0

# 5) 6

# 6) the finally block will be executed no matter if the try block raises an error or not.

# 7) It is used to raise an exception.

# 8) in defining a generator.

# 9) _abc and abc2

# 10) yield and raise

# 11)

# In[1]:


number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i
    
print("The factorial of", number, "is", factorial)


# 12)

# In[2]:


new_number = 26

def prime_or_composite(new_number):
    if new_number <= 1:
        return False
    for i in range(2, number):
        if new_number % i == 0:
            return False
    return True

if prime_or_composite(new_number):
    print(str(new_number) + " is a prime number.")
else:
    print(str(new_number) + " is a composite number.")


# 13)

# In[3]:


def palindrome(s):
    return s == s[::-1]

s = "level"
ans = palindrome(s)
 
if ans:
    print("Yes, the word is palindrome")
else:
    print("No, the word isn't palindrome")


# 14)

# In[4]:


def find_side(side1, side2):
  
    third_side = (side1 ** 2 + side2 ** 2) ** 0.5
    return third_side

side1 = 3
side2 = 4

third_side = find_side(side1, side2)

print(third_side)


# 15)

# In[6]:


Data = "ILovePython"
 
frequency = {}
 
for i in Data:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

print("frequency in ILovePython = " + str(frequency))

