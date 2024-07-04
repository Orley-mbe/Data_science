#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Используя цикл, создать список, содержащий все целые числа от 1 до 10, и вывести его на экран.


# In[6]:


#метод 1 (сложность алгоритма O(n))
list_number = []
for el in range(1,11):
    list_number.append(el)
print(list_number)
    


# In[ ]:


#метод 2 (сложность алгоритма O(n))
list_number = []
el=0
while el <=10:
    list_number.append(el)
    el=el+1
print(list_number)


# In[ ]:




