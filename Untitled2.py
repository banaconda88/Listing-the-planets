#!/usr/bin/env python
# coding: utf-8

# In[30]:


file = open('planets.txt')
planets = file.read().split()


# In[36]:


for p in planets:
    print(p, ", ", len(p), ", ", len(p)*2, sep="")

