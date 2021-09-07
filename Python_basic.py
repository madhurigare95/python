#!/usr/bin/env python
# coding: utf-8

# In[ ]:


A = {1,2,3,'Madhu'}
print(A)


# In[ ]:


2+3


# In[ ]:


8/4


# In[ ]:


9-2


# In[ ]:


2.5/2.5 #follows floor division


# In[ ]:


2**2 #power of indices


# In[ ]:


6*2.1


# In[ ]:


(6+2)*1 #BODMAS rule


# In[ ]:


2**4


# In[ ]:


10//3 #gives reminder


# In[ ]:


10%3 #modulus


# In[ ]:


'Madhu'+'ri'


# In[ ]:


5*'Madhu'


# In[ ]:


print('C:\docs\navin')http://localhost:8888/notebooks/Basics%20of%20Python.ipynb#


# In[ ]:


print('Hello \b World')


# In[ ]:


print('Hello \br World!')


# In[ ]:


print(r'Hello there!')


# In[ ]:


X=9


# In[ ]:


X+5


# In[ ]:


Y=9
X+Y


# In[ ]:


_+9 #when we need to increment/decrement of previous value
    #_ fetches previous value


# In[ ]:


_/9


# In[ ]:


(_**2) +2


# In[ ]:


Z = 'abc'
a = _+Z


# In[ ]:


name = 'Madhuri'
name + ' G'


# In[ ]:


name [3] #indexing


# In[ ]:


name [-7]


# In[ ]:


name


# In[ ]:


_ + 'Gare'


# In[ ]:


name[3] = 'a'


# In[ ]:


name.insert(2,a)


# In[ ]:


name[0:2] + 'a' + name[2:10]


# In[ ]:


#interview questions
names = ['Madhu','Viggy','Rito']
names


# In[ ]:


nums = [10,20,30]
ba = [nums, names]
ba


# In[ ]:


nums.append(45)
nums


# In[ ]:


nums.remove(45)
nums


# In[ ]:


nums.pop()
nums


# In[ ]:


nums.pop()
nums


# In[ ]:


nums = [10,20,30,40,50]
nums


# nums.insert(60)
# nums

# In[ ]:


nums.insert(2,60) 
nums


# In[ ]:


del nums [2:]
nums


# In[ ]:


nums.extend([12,24,36,48])
nums


# In[ ]:


#3 Sep
x = 2
y = 3
z = x+y
print(z)


# In[ ]:


nums


# In[ ]:


nums.extend([100,90,80,70,60,50])
nums


# In[ ]:


min(nums)


# In[ ]:


max(nums)


# In[ ]:


nums.sort()
nums


# In[ ]:


nums.sort(reverse=True)
nums


# In[ ]:


tup = (21,31,41,51,61)
tup


# In[ ]:


tup[3]


# In[ ]:


tup.append(71)


# In[ ]:


tup.index()


# In[ ]:


a = 'hello'
a
print(a)


# In[ ]:


type(a)


# In[ ]:


a = ('hello','madhu')
a


# In[ ]:


type(a)


# In[ ]:


isinstance(a,tup)


# In[ ]:


#Sets
s = {22,25,14,51,41}
s

type(s)


# In[ ]:


W = {14,23,12,13,24}
print(W)


# In[ ]:


E = {23,25,28,75,54,69,69,88,88}
print(E)
#eliminates duplicates


# In[ ]:


#Dictionary
data = {1:"Avinash",2:"Maneesh",3:"Viggy"}
type(data)


# In[ ]:


data[2]


# In[ ]:


data.get(3)


# In[ ]:


data.get(5,"not found")


# In[ ]:


keys = {'Tanmay','Kiran','Madhuri','Madhuri','Poulomi'}
print(keys)
values = {'leader 1','Manager','Analyst', 'Audience'}


# In[ ]:


data = dict(zip (keys, values))
data


# In[ ]:


data['Madhuri']


# In[ ]:


tu=tup+(a,)
tu


# In[ ]:


data.keys()


# In[ ]:


data.values()


# In[ ]:


data.items()


# In[ ]:


data.update({'raj':'audience'})
data


# In[ ]:


data.pop('Kiran')
data


# In[ ]:


university={'JS':180,"CS":80,"CMS":["BA","FIN","MKT"]}
university


# In[ ]:


university['CS']


# In[ ]:


import math
X=math.sqrt(25)
X


# In[ ]:


print(math.pi)


# In[ ]:


print(math.e)


# In[ ]:


#7 Sep
#math functions
import math
x = math.sqrt(59)
x


# In[ ]:


x = round(math.sqrt(59))
x


# In[ ]:


x = math.sqrt(59)
print(math.floor(x))


# In[ ]:


print(math.ceil(x))


# In[ ]:


x = 2**2
x


# In[ ]:


pow(2,2)


# In[ ]:


x = pow(math.sqrt(25), 2)
x


# In[ ]:


help(math)


# In[ ]:


#calculator application- interactive

x = int(input("Enter 1st number"))
y = int(input("Enter 2nd number"))
z = x+y
print(z)


# In[ ]:


result = eval ( input("Enter an expression "))
print(result)


# In[ ]:


ch = input("Enter a char ")
print(ch[0])


# In[ ]:


#if condition

if True:
    print ('I am Madhuri')
if False:
    print ('I am a Robot')


# In[ ]:


x = 3
r = x%2

if r == 0:
    print('True') #even
if r == 1:
    print('False') #odd


# In[ ]:


x = int(input("Enter a number "))
if x >= 10:
    print('Enter a value less than 10')   
else:
    r = x%2

    if r == 0:
        print('I am Madhuri') #even
    if r == 1:
        print('I am a robot') #odd


# In[ ]:


#while loop
#increment

i = 1
while i<=10:
    print("I'm coding in Python",i)
    i = i+1


# In[ ]:


#decrement

i = 5
while i>=1:
    print("I'm coding in Python",i)
    i = i-1


# In[ ]:


i=5, j=1
while i<=5:
    print("Me Myself & I")
while j<=4:
    print("I Me")
    j=j+1
    i+i+1


# In[ ]:


i = 1
while i<4:
    print("Tanmay Jain ",end="")
    i=i+1


# In[ ]:


i = 1
j=1
while i<=3:
    while j<=3:
        print("Hello", end=" ")
        print("World",end=" ")
        j=j+1
        i=i+1


# In[ ]:


#for loop

x = ['Hello',65,4.5]
for i in x:
    print(i)


# In[4]:


x = 'Hello'
for i in x:
    print(i)


# In[5]:


x ={'hello',65,4.5,65}
for i in x:
    print(i)


# In[13]:


for i in range(10):
    print(i)


# In[14]:


for i in range(3,10):
    print(i)


# In[17]:


for i in range(11,21,1):
    print(i)


# In[20]:


import numpy as np

for i in np.arange(10.5):
    print(i)


# In[21]:


for i in range(1,21):
    if i%5!=0:
        print(i)


# In[34]:


for i in range(10, 16):
    print(i)
    print(i+0.5)


# In[ ]:




