#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# question 1

a = input("Enter a string")
b = a[::-1]
print(b)


# In[ ]:


# question 2

rang = int(input("Enter the range"))
num_1 = int(input("Enter the number divisible by"))
for i in range(1,rang):
    if i%num_1==0:
        print(i)
    else:
        print("error")


# In[ ]:


# question 3

a= float (input("enter the side 1: "))
b= float (input("enter the side 2: "))
c= float (input("enter the side 3: "))
if a+b>c and b+c>a and c+a>b:
    s = (a+b+c)/2
    area = (s*(s-a)*(s-b)*(s-c))**(0.5)
    print(area)
else:
    print("error")


# In[ ]:


# question 4

for i in range(5):
    for j in range(i+1):
        print("* ", end="")
        print("\n")
    for a in range (4,0,-1):
    for b in range (0,a):
        print("* ",end="")
        print("\n")


# In[ ]:


# question 5

rows = int(input("Enter number of rows= "))
alphabet = 65
for i in range(rows):
    for j in range(i=1):
        print(chr(alphabet), end="")
        alphabet+=1
    print(" ")
        


# In[ ]:


# question 6

rang = int(input("Enter the range "))
for i in range(rang):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)


# In[ ]:


# question 7

for i in range(1,501):
    if i%7==0 and i%11==0:
        print(i)


# In[ ]:


# question 8

a=input('Enter 10 integers ').split(' ')
positive=[]
negative=[]
odd=[]
even=[]
for i in a:
    i=int(i)
    if i>0:
        positive.append(i)
print('The positive numbers are: ',positive)

for i in a:
    i=int(i)
    if i<0:
        negative.append(i)
print('The negative numbers are: ', negative)

for i in a:
    i=int(i)
    if i%2==0:
        even.append(i)
print('The even numbers are: ',even)

for i in a:
    i=int(i)
    if i%2==1:
        odd.append(i)
print('The odd numbers are: ',odd)


# In[ ]:


# question 9

a = input(str("enter a string: "))

def word_count(line):
    counts = dict()
    words = line.split()
    for word in words :
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
    
print(word_count(a))

