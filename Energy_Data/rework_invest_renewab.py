#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 08:39:48 2020

@author: annalena
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('raw_data/Bloomberg_inv_renew.csv')

# Renaming due to the usage as polt lables.
df = df.rename(columns={'year': 'Year'})

# List of all countries to seperate the data for plotting.
countries = pd.Series(df.country).unique()

for x in countries:
     
    # Investment average per year by country.
    countryRelatedData = df[df['country'] == x]
    groupingByYear = countryRelatedData.groupby([countryRelatedData.Year, 'country'])['value'].mean().reset_index(name='Yearly Average')
    
    # Without plt.figure() all plots are in the same window.
    plt.figure()
    sns.lineplot(x='Year', y='Yearly Average', data=groupingByYear).set_title('Renewable Energy Investment ' + x + ' (B USD)')
