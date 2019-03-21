#!/usr/bin/env python
# coding: utf-8

# In[26]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 8.0)

# Reading Data
data = pd.read_csv('G:/claim2.csv')
print(data.shape)
data.head()


# In[27]:


X = data['age'].values
Y = data['charges'].values


# In[28]:


# Mean X and Y
mean_x = np.mean(X)
mean_y = np.mean(Y)

# Total number of values
m = len(X)

# Using the formula to calculate b1 and b2
numer = 0
denom = 0
for i in range(m):
    numer += (X[i] - mean_x) * (Y[i] - mean_y)
    denom += (X[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

# Print coefficients
print(b1, b0)


# In[29]:


max_x = np.max(X) 
min_x = np.min(X) 

# Calculating line values x and y
x = np.linspace(min_x, max_x, 10)
y = b0 + b1 * x

# Ploting Line
plt.plot(x, y, color='#58b970', label='regression line')
# Ploting Scatter Points
plt.scatter(X, Y, c='#ef5423', label='scatter plot')

plt.xlabel('age')
plt.ylabel('charges')
plt.legend()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




