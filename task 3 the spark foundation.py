#!/usr/bin/env python
# coding: utf-8

# # Author:G MADHU CHANDANA
# To Explore Buisness Analytics
# Objective:
# ● Perform ‘Exploratory Data Analysis’ on dataset ‘SampleSuperstore’
# 
# ● As a business manager, try to find out the weak areas where you can work to make more profit.
# 
# ● What all business problems you can derive by exploring the data?

# # Importing the libraries

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# In[11]:


dataset =  pd.read_csv(r'C:\Users\USER\Downloads\SampleSuperstore.csv')
dataset.head()


# In[12]:


dataset.describe()


# # Handling missing data

# In[13]:


dataset.isnull().sum()


# # Handling duplicate records

# In[14]:


duplicate=dataset.duplicated()
print(duplicate.sum())
dataset[duplicate]


# In[15]:


dataset.drop_duplicates(inplace=True)


# In[16]:


dpl=dataset.duplicated()
dpl.sum()


# # Handling outliers

# In[17]:


dataset.boxplot(column=["Sales"])
plt.show()


# # Removing outliers

# In[19]:


def remove_outlier(col):
  sorted(col)
  q1,q3=col.quantile([0.25,0.75])
  IQR=q3-q1
  lower_range=q1-(1.5*IQR)
  upper_range=q3+(1.5*IQR)
  return lower_range, upper_range


# In[20]:


lowsales,upsales=remove_outlier(dataset['Sales'])
dataset['Sales']=np.where(dataset['Sales']>upsales,upsales,dataset['Sales'])
dataset['Sales']=np.where(dataset['Sales']<lowsales,lowsales,dataset['Sales'])


# In[21]:


dataset.boxplot(column=["Sales"])
plt.show


# In[22]:


dataset.boxplot(column=["Profit"])
plt.show()


# In[24]:


lowprofit,upprofit=remove_outlier(dataset['Profit'])
dataset['Profit']=np.where(dataset['Profit']>upprofit,upprofit,dataset['Profit'])
dataset['Profit']=np.where(dataset['Profit']<lowprofit,lowprofit,dataset['Profit'])


# In[25]:


dataset.boxplot(column=["Profit"])
plt.show()


# In[26]:


fig, axes = plt.subplots(1,1, figsize = (8,5))
sns.heatmap(dataset.corr())
plt.show()

Here we can see discount and profit are highly negative corelated. Values closer to zero means there is no linear trend between the two variables. The values Closer to 1 the correlation is the more positive. A correlation closer to -1 is similar, but instead of both increasing one variable will decrease as the other increases

Here we can see discount and profit are highly negatively corelated
Sales and Profits are Moderately Correlated
Quantity and Profit are Moderately Correlated
# In[27]:


plt.figure(figsize=(10,10))
dataset.groupby('Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.show()


# In[28]:


plt.figure(figsize=(10,10))
dataset.groupby('Sub-Category')['Profit','Sales'].agg(['sum']).plot.bar()
plt.show()

We see that paper has maximum amount of profit with comparatively lesser sales. Whereas, tables experiences no profit at all with the sales around 2 lakh.
# In[29]:


plt.figure(figsize=(24,10))
dataset.groupby('Sub-Category')['Profit'].agg(['sum']).plot.bar()
plt.show()

In the above sub-category section, with respect to profit:

1) Tablets are expereincing loss

2) Supplies produces the least amout of profit

3) PAPER produces maximum profit


# In[30]:


sns.barplot(x=dataset.Discount,y=dataset.Profit)

When we compare the profit with respect to discounts, all the discounts above 20% is facing a major loss
# In[31]:


sns.barplot(x=dataset.Region, y=dataset.Profit,hue=dataset.Category)

When we perform a bivariate analsyis of region and category with respect to profit, we can conclude from the above graph that:

1) Furniture is facing loss in the Central region

2) Technology gets maximum profit in the Southern region.
# In[32]:


dataplot = dataset.groupby(['State'])['Sales', 'Profit'].sum()
dataplot.plot.bar(figsize = (20,10))

When the data of different states is analysed, we can conclude that California recieves maximum amount of profit with maximum sales when compared to the other states.
# In[33]:


dataset['Ship Mode'].value_counts()


# In[34]:


(dataset['Ship Mode'].value_counts()/len(dataset['Ship Mode']))*100


# In[35]:


((dataset['Ship Mode'].value_counts()/len(dataset['Ship Mode']))*100).plot(kind="bar", color="blue")


Conclusions when the ship mode data is analysed:

1) Maximum number of shipments belong to tha standard class

2) whereas, very less number of shipments are done on the same day (10%)
# In[36]:


dataset['Category'].value_counts()


# In[37]:


(dataset['Category'].value_counts()/len(dataset['Category']))*100


# In[38]:


((dataset['Category'].value_counts()/len(dataset['Category']))*100).plot(kind="bar", color="yellow")

In the Category Section:

1) Almost 60% of products belong to Office supplies

2) Almost 18% of product belong to Technology which is the minimum