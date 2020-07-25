#!/usr/bin/env python
# coding: utf-8

# In[16]:


#Problem 1
list1=['hi', 7, True,-23,False,1.38,True]
x=input()
print(f"Number of {x}s is",str(list1).count(x))


# In[23]:


#Problem 2
t1=('hi', 7, True,-23,False,1.38,True)
t2=t1[:4]
t2+=('hello',)
t2+=t1[5:]
t1=t2
del t2
print(t1)


# In[30]:


#Problem 3
d={"name":"Armen","age":15, "grades":[10,8,8,4,6,7]}
if 'weight' in d.keys():
    print(d['weight'])
else:
    d['weight']=int(input())


# In[36]:


#Problem 4
correct_num=5
for i in range(0,10):
    guess=int(input())
    if guess==correct_num:
        print("That was a good guess!")
        break
    else:
        continue #else is optional


# In[43]:


#Problem 5
list1=['a', 'abc', 'xyz', 's', 'aba', '1221']
print(len([el for el in list1 if len(el)>2 and el[0]==el[-1]]))

