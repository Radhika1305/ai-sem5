#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("062_Radhika Shrivastava")
def factorial(num):
    ans=1
    if num<0:
        return -1
    elif num==0:
        return 1
    else:
        for i in range(1, num+1):
            ans=ans*i
        return ans
num = input("Enter a number (q to quit): ")
fac=0
while(num!='q'):
    num = int(num)
    fac = factorial(num)
    if fac<1:
        print("Factorial of negative number doesn't exist.")
    else:
        print("Factorial of ",num," is ", fac)
    num = input("Enter a number (q to quit): ")


# In[ ]:




