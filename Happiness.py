#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:52:06 2018

@author: vlad
"""



import os
os.chdir('/Users/vlad/Projects/Happiness')
import pandas as pd
import numpy as np
import matplotlib as plt


data_15 = pd.read_csv('2015.csv')
data_16 = pd.read_csv('2016.csv')
data_17 = pd.read_csv('2017.csv')
data_15['Year'] = 2015
data_16['Year'] = 2016
data_17['Year'] = 2017

data_15.drop('Standard Error', axis = 1, inplace = True)
data_16.drop(['Lower Confidence Interval', 'Upper Confidence Interval'], axis = 1, inplace = True)
data_17.drop(['Whisker.high','Whisker.low',], axis = 1, inplace = True)

#list(data_17.columns.values)

data_17.columns = ['Country','Happiness Rank','Happiness Score',
 'Economy (GDP per Capita)',
 'Family',
 'Health (Life Expectancy)',
 'Freedom',
 'Generosity',
 'Trust (Government Corruption)',
 'Dystopia Residual',
 'Year']

data_17['Region'] = ''
data_17 = data_17[list(data_16.columns.values)]

country = data_15['Country']
region = data_15['Region']
country_dict = dict(zip(country, region))
data_17.loc[:,'Region'] = data_17.loc[:,'Country']
data_17['Region'].replace(country_dict, inplace = True)

data_17.loc[data_17['Region'] == 'Belize', 'Region'] = 'Latin America and Caribbean'
data_17.loc[data_17['Region'] == 'Hong Kong S.A.R., China', 'Region'] = 'Eastern Asia'
data_17.loc[data_17['Region'] == 'Namibia', 'Region'] = 'Sub-Saharan Africa'
data_17.loc[data_17['Region'] == 'Somalia', 'Region'] = 'Middle East and Northern Africa'
data_17.loc[data_17['Region'] == 'South Sudan', 'Region'] = 'Sub-Saharan Africa'
data_17.loc[data_17['Region'] == 'Taiwan Province of China', 'Region'] = 'Eastern Asia'



df = pd.concat([data_15, data_16, data_17], axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)


GDP = df.pivot_table(values = 'Economy (GDP per Capita)', index = 'Region', columns = 'Year', aggfunc = np.mean)
Happiness = df.pivot_table(values = 'Happiness Score', index = 'Region', columns = 'Year', aggfunc = np.mean)

GDP.sort_values(by =2017, ascending = False, inplace = True)
Happiness = Happiness.reindex(labels = GDP.index)

happy = Happiness.plot(kind = 'barh')
fig = happy.get_figure()
fig.savefig('happy.png')
gdp = GDP.plot(kind = 'barh')
fig = gdp.get_figure()
fig.savefig('gdp.png')
