# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:32:59 2020

@author: Joris Dreesen
"""


import pandas as pd
import pandas_datareader as web
import datetime as dt
import random 
import numpy as np 
import statistics
import matplotlib.pyplot as plt
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')
ticker = 'TSLA' 
OHLC = web.get_data_yahoo(ticker,
                            start = "1980-01-01",
                            end = today)

daily_returnsABS = OHLC['Adj Close']
daily_returns = OHLC['Adj Close'].pct_change()

stdeviation = daily_returns.std()
mean = daily_returns.mean()

#TESTER 

meanPLs = []

for g in range(10):
    
    S0 = daily_returnsABS.iloc[-1] 
    
    
    Array = []
    
    #Array = np.insert(Array,0,S0)
    
    y = 756
    
    for x in range(y):
        rand_rets = np.random.normal(mean,stdeviation,100) 
        Array.append(rand_rets)
    
    # plt.plot(Array)
    # plt.hist(Array, 20,
    #           density=True,
    #           histtype='bar')
    
    # plt.show()
    
    price_list = np.zeros_like(Array)
    price_list[0] 
    price_list[0] = S0 
    price_list
    
for t in range(1, y):
    price_list[t] = price_list[t - 1] + (price_list[t - 1] * Array[t])
        
plt.plot(price_list)
plt.title(ticker)
plt.axhline(y= S0, color='r', linestyle='-')
plt.show()
    
meanPL = price_list.mean()
meanPLs.append(meanPL)
    
print('Currrent Price is:',round(S0, 2), ",Expected Price Monte Carlo:", round(meanPL, 2))
    
# plt.plot(Array)
# plt.hist(Array, 20,
#            density=True,
#            histtype='bar')
    
# plt.show()
