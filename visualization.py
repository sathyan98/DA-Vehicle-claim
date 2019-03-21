#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('G:\project.csv')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[23]:


df3.info()


# In[24]:


df3.head()


# In[25]:


df3.head()


# In[26]:


df3.plot.scatter(x='age',y='charges',s=50,c='red')


# In[27]:


df3['age'].plot.hist(bins=20)


# In[28]:


df3['region'].plot.hist(bins=10)


# In[29]:


df3.plot.area(alpha=0.4)


# In[30]:


df3.plot.bar()


# In[31]:


df3.plot.scatter(x='age',y='sex',c='bmi',cmap='coolwarm')


# In[32]:


df3.plot.density()


# In[34]:


import pandas as pd
import matplotlib.pyplot as plt
df3 = pd.read_csv('G:\project.csv')
get_ipython().run_line_magic('matplotlib', 'inline')


# df3.head()

# In[35]:


df3.head()


# In[36]:


df3.head()


# In[37]:


df3.plot.scatter(x='age',y='sex',c='children')


# In[38]:


df3.plot.scatter(x='region',y='children',s=90,c='yellow')


# In[21]:


df3.plot.bar(alpha = 0.4)


# In[25]:


df3.plot.bar(alpha = 1.0)

