#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


# In[117]:


tickers = ['HD','DIS','WMT','VZ']


# In[118]:


weights = np.array([.25, .3, .15, .3])


# In[119]:


initial_investment = 1000


# In[120]:


start = dt.datetime(2020,1,1)
end = dt.datetime(2020,12,31)


# In[121]:


data = pdr.get_data_yahoo(tickers, start, end=dt.date.today())['Close']


# In[122]:


returns = data.pct_change()


# In[123]:


returns.tail()


# In[124]:


cov_matrix = returns.cov()
cov_matrix


# ### Calculating Means

# In[125]:


avg_rets = returns.mean()


# In[126]:


port_mean = avg_rets.dot(weights)

 

# Calculate portfolio standard deviation

port_stdev = np.sqrt(weights.T.dot(cov_matrix).dot(weights))

 

# Calculate mean of investment

mean_investment = (1+port_mean) * initial_investment

             

# Calculate standard deviation of investmnet

stdev_investment = initial_investment * port_stdev


# ### Confidence Level

# In[142]:


# Select our confidence interval (I'll choose 95% here)

conf_level1 = 0.05


from scipy.stats import norm

cutoff1 = norm.ppf(conf_level1, mean_investment, stdev_investment)


# ### 95% Confidence

# In[143]:


#Finally, we can calculate the VaR at our confidence interval

var_1d1 = initial_investment - cutoff1

var_1d1


# In[140]:


# Calculate n Day VaR

var_array = []
num_days = int(15)

for x in range(1, num_days+1):    
    var_array.append(np.round(var_1d1 * np.sqrt(x),2))
    print(str(x) + " day VaR @ 95% confidence: " + str(np.round(var_1d1 * np.sqrt(x),2)))


# In[139]:


plt.xlabel("Day #")
plt.ylabel("Max portfolio loss (USD)")
plt.title("Max portfolio loss (VaR) over 15-day period")
plt.plot(var_array, "r")


# In[130]:


import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats
import scipy as sp


# In[138]:


returns['HD'].hist(bins=40, histtype="stepfilled",alpha=0.5)
x = np.linspace(port_mean - 3*port_stdev, port_mean+3*port_stdev,100)
plt.plot(x, sp.stats.norm.pdf(x, port_mean, port_stdev), "r")
plt.title("HD returns (binned) vs. normal distribution")
plt.show()


# In[137]:


returns['DIS'].hist(bins=40, histtype="stepfilled",alpha=0.5)
x = np.linspace(port_mean - 3*port_stdev, port_mean+3*port_stdev,100)
plt.plot(x, sp.stats.norm.pdf(x, port_mean, port_stdev), "r")
plt.title("DIS returns (binned) vs. normal distribution")
plt.show()


# In[136]:


returns['WMT'].hist(bins=40, histtype="stepfilled",alpha=0.5)
x = np.linspace(port_mean - 3*port_stdev, port_mean+3*port_stdev,100)
plt.plot(x, sp.stats.norm.pdf(x, port_mean, port_stdev), "r")
plt.title("WMT returns (binned) vs. normal distribution")
plt.show()


# In[135]:


returns['VZ'].hist(bins=40, histtype="stepfilled",alpha=0.5)
x = np.linspace(port_mean - 3*port_stdev, port_mean+3*port_stdev,100)
plt.plot(x, sp.stats.norm.pdf(x, port_mean, port_stdev), "r")
plt.title("VZ returns (binned) vs. normal distribution")
plt.show()


# ### Source
# #### https://www.interviewqs.com/blog/value_at_risk

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




