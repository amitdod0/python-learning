#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Write a program to print all numbers from 1 to 50 using a for loop.

for a in range(1,51):
    print(a)


# In[ ]:


#Write a program to print all even numbers between 1 and 100.
n = 100
for i=1 i<n i++:
       if ( i%2 == 0 )
         print(i++)


# In[ ]:


for numbers in range(1,101):
    if numbers%2==0:
        print(numbers)


# In[ ]:


#Create a program to calculate the sum of all numbers in a list. Example:
numbers = [1,45,96,78]
total=0
for number in numbers:
    total=total+number
    
print(total)


# In[1]:


#Write a program to calculate the factorial of a number using a while loop. 
n = int(input("Enter a number: "))
result = 1

while n > 0:
    result=result*n  # Multiply result by n
    n=n-1  

print("The factorial is:", result)


# In[14]:


numbers = [4, 10, 2, 8, 6]

max_num = numbers[0]
for n in numbers:
    if max_num = n if n >== max_num 
        else max_num
        print(n)
    
        


# In[15]:


#Create a dictionary to store names and scores of students. Write a program to search for a student’s score by their name.
students = {
 "name": "amit",
 "sub": "ai",
 "marks": 80
}


search = input("enter the students name for search")

if search in students["name"]:
   print(f"Name: {students['name']}, Subject: {students['sub']}, Marks: {students['marks']}")
else:
   print('nothing found')


# In[18]:


def even(num):
    if num%2==0:
        print("it's even number")
    else:
        print("it's not even")
    return num


print(result)
result = even(8)


# In[ ]:




