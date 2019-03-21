#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.preprocessing import Imputer
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('G:\project.csv')
df.info()


# In[3]:


x = df.iloc[:,:-1].values
y = df.iloc[:,-1].values


# In[4]:


imp = Imputer(strategy="mean",axis=0,missing_values= 'NaN')
x = imp.fit_transform(x)
x

