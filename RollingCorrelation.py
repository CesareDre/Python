# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 12:16:37 2020

@author: Joris Dreesen
"""

import datetime
import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import seaborn as sn
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio


start = '2020-01-01'
end = '2021-12-29'
 
tickers = ['CL=F','^GSPC','^VIX','SPY','^TNX']

price_data = []
for ticker in tickers:
    try:
        prices = wb.DataReader(ticker, start = start, end = end, data_source='yahoo')[['Adj Close']]
        price_data.append(prices.assign(ticker=ticker)[['ticker', 'Adj Close']])
    except:
        pass

names = pd.concat(price_data)
names.reset_index()
names

df = pd.concat(price_data)

pd.set_option('display.max_columns', 525)

df = df.reset_index()
df = df.set_index('Date')
table = df.pivot(columns='ticker')

table1 =table.sum(level=1,axis=1)

CorVar1= '^GSPC'
CorVar2 = 'SPY'

rollingcorr = pd.Series(table1[CorVar1].rolling(10).corr(table1[CorVar2]),name ='Correlation '+str(CorVar1)+' & '+str(CorVar2))

fig = px.line(rollingcorr)

df = df.dropna()
fig.show()