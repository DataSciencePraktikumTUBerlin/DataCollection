#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 08:39:48 2020

@author: annalena
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('invest_renewab.csv')
df = df.rename(columns={'year': 'Year'})

countries = pd.Series(df.country).unique()
print(countries)


for x in countries:
    countryRelatedData = df[df['country'] == x]
    groupingByYear = countryRelatedData.groupby([countryRelatedData.Year, 'country'])['value'].mean().reset_index(name='Yearly Average')
    plt.figure()
    sns.lineplot(x='Year', y='Yearly Average', data=groupingByYear).set_title('Renewable Energy Investment ' + x + ' (B USD)')
