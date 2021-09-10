#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd

from pandas import read_csv
from pandas.plotting import scatter_matrix
from scipy.stats import ttest_ind

url= "https://raw.githubusercontent.com/iisydnii/Data_Analytics_Excerise_3/main/Income%20Data.csv"
dataset = pd.read_csv(url, error_bad_lines=False)
print("Sydni's Exercise 3")
print("09/10/2021")


print("")
print(dataset.head())


print("")
print("Minimum value for each column")
minValueObj = dataset.min()
print(minValueObj[2:].to_string())

print("")
print("Maximum value for each column")
maxValueObj = dataset.max()
print(maxValueObj[2:].to_string())

print("")
print("Mean value for each column")
meanValueObj = dataset.mean()
print(meanValueObj[0:].to_string())

print("")
print("Median value for each column")
medianValueObj = dataset.median()
print(medianValueObj[0:].to_string())

print("")
print("1st and 3rd quartiles value for each column")
quantileValueObj = dataset[1:].quantile([.25, .75])
print(quantileValueObj.to_string())

print("")
print("Standard deviation value for income")
print(round(dataset["income"].std(),2))

print("")
print("Variance value for income")
print(round(dataset["income"].var(),2))

print("")
print("correlation coefficients value for income and education")
print(dataset.loc[:, "income":"education"].corr().to_string())

print("")
print("p-values for income and education")
print(ttest_ind(dataset['income'], dataset['education'])[1])


print("")
print("plot histogram")
dataset.hist(column="prestige")

print("")
print("Plot income and education")
dataset.plot(y=["education", "income"])


# In[ ]:





# In[ ]:




