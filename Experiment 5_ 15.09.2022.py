#!/usr/bin/env python
# coding: utf-8

# Magic square problem

# In[6]:


def generateSquare(n):
    magicSquare=[[0 for x in range(n)]
                for y in range(n)]
    i=n/2
    j=n-1
    num=1
    while num<= (n*n):
        if i== -1 and j==n:#reaches the end of row and column
            j=n-2
            i=0
        elif j==n: #reaches the end of column
            j=0
        if i<0: #reaches the end of row
            i=n-1
        if magicSquare[int(i)][int(j)]: #if square is already assigned a number
            j=j-2
            i=i+1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num=num+1
        j=j+1
        i=i-1
        
    for i in range(0,n):
        for j in range(0,n):
            print('%2d' % (magicSquare[i][j]), end='')
            if j==n-1:
                print()
n=3
print("062_Radhika Shrivastava")
print("Magic Square for n = ",n)
print("Sum of each row or column ", n*(n*n+1)/2,"\n")
generateSquare(n)


# In[ ]:




