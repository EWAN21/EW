#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math

r = float(input("Please enter the radius of the circle（mm）："))
s = round(2 * r * math.pi,2)
a = round(math.pi * r**2,2)
print("The circumference of the circle：{}mm".format(s))
print("The area of a circle{}mm^2".format(a))


# In[ ]:


def uppercase_lowercase(string):
  uppercase = 0
  lowercase = 0
  for char in string:
    if char.islower():
      lowercase += 1
    elif char.isupper():
      uppercase +=1
    
  return(uppercase, lowercase)

print(uppercase_lowercase('Hello World'))


# In[ ]:




