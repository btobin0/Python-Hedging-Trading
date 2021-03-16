#!/usr/bin/env python
# coding: utf-8

# In[58]:


import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import statistics 
from statistics import mode
import seaborn as sns


# In[19]:


tickers = ['HD']


# In[20]:


weights = np.array([.25, .3, .15, .3])


# In[21]:


initial_investment = 1000


# In[30]:


start = dt.datetime(2020,1,1)
end = dt.datetime(2020,12,31)


# In[23]:


data = pdr.get_data_yahoo(tickers, start, end=dt.date.today())['Close']


# In[33]:


df = pd.DataFrame(data)


# In[36]:


print(df)


# # Statistics and The Market

# # # Central Tendency

# In[37]:


df.mean()


# In[38]:


df.median()


# In[46]:


statistics.mode(data)


# ## Dispersion

# In[50]:


df.var() # Variance


# In[49]:


df.std() # Standard Deviation


# In[64]:


df.max()


# In[65]:


df.min()


# In[66]:


df.max()-df.min() #Range


# In[67]:


df.quantile() #InterQuartile


# ## Skew

# In[55]:


df.skew()


# ## Kurtosis

# In[56]:


df.kurt()


# In[63]:


sns.distplot(df,hist=True,kde=True) 
# Pricing is Skewed at Left Skewed from lower stock price rising, 
    # but becomes somewhat equal to ND as the higher stock price becomes more stable. 


# ## Source

# ### https://dataanalyticsedge.com/2019/11/25/descriptive-statistics-using-python/

# In[ ]:




