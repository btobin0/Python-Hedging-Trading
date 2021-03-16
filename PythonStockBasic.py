#!/usr/bin/env python
# coding: utf-8

# In[50]:


import yfinance as yf
import pandas as pd


# In[2]:


tickerSymbol = 'MSFT'


# In[3]:


tickerData = yf.Ticker(tickerSymbol)


# In[46]:


tickerDf = tickerData.history(period='1d', start='2020-12-3', end='2020-12-4')


# In[47]:


tickerDf


# In[48]:


tickerData.recommendations


# In[22]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[26]:


data = yf.download('MSFT','2019-12-03','2020-12-04')


# In[27]:


data['Adj Close'].plot()


# In[29]:


ticker_list = ['HD', 'DIS','MSFT','VZ']


# In[30]:


dataList = yf.download(ticker_list,'2019-12-03','2020-12-04')


# In[33]:


print(dataList.head)


# In[31]:


dataList['Adj Close'].plot()


# In[40]:


((dataList.pct_change()+1).cumprod()).plot(figsize=(20,20))
plt.legend()
plt.title("Returns", fontsize=16)
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# In[54]:


((data.pct_change()+1).cumprod()).plot(figsize=(15,40))
plt.legend()
plt.title("Returns", fontsize=16)
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# In[60]:


minData = yf.download(tickers="MSFT", period="1d", start='2020-12-3', end='2020-12-4', interval="1m")


# In[61]:


data['Volume'].plot()


# In[63]:


((minData.pct_change()+1).cumprod()).plot(figsize=(15,10))
plt.legend()
plt.title("Returns", fontsize=16)
plt.ylabel('Cumulative Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()


# In[ ]:




