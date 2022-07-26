# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 09:19:26 2022

@author: Shubham
"""

import pandas as pd

import os 

os.chdir(r"D:\Data Analyst\Python Project")
os.listdir()

Police = pd.read_csv("Police Data.csv")
Police

# Remove the column that only contains missing values.

Police.isnull().sum()

Police.drop(columns = 'country_name', inplace = True)

# For Speeding, were Men or Women stopped more oftern 

Police[Police.violation == 'Speeding'].driver_gender.value_counts()

# Does gender affect who gets searched during a step ?

Police.groupby('driver_gender').search_conducted.sum()

Police.search_conducted.value_counts()

# What is the mean stop_duration ?

Police.stop_duration.value_counts()

Police['stop_duration'] = Police['stop_duration'].map( {'0-15 Min' : 7.5, '16-30 Min' : 24, '30+ Min' : 45})
Police

Police['stop_duration'].mean()

# Compare the age distributions fro each violation:
    
Police.groupby('violation').driver_age.describe()
