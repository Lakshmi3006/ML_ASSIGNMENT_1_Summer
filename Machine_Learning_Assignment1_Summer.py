#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Read the provided CSV file ‘data.csv’.

import pandas as pd
df = pd.read_csv('data.csv')     #reading csv file
df


# In[2]:


#Show the basic statistical description about the data.

df.describe()   #describe() results statistical description of data in data frame


# In[3]:


#Check if the data has null values.

df.isnull().any()  #check any column has null values


# In[4]:


#Replace the null values with the mean

mean=df['Calories'].mean()
df['Calories'].fillna(value=mean, inplace=True)  #replacing Nan values with particular columns mean value


# In[5]:


df.isnull().any()


# In[6]:


#Select at least two columns and aggregate the data using: min, max, count, mean.

df.agg({'Pulse' : ['min', 'max', 'count', 'mean'], 'Maxpulse' : ['min', 'max', 'count', 'mean'], 
        'Calories' : ['min', 'max', 'count', 'mean'] })
#agg method to aggreate operation on the dataframe


# In[7]:


#Filter the dataframe to select the rows with calories values between 500 and 1000. 

df[(df['Calories'] > 500) & (df['Calories'] < 1000)]   #'&' operator to filter the dataframe


# In[8]:


#Filter the dataframe to select the rows with calories values > 500 and pulse < 100.

df[(df['Calories'] > 500) & (df['Pulse'] < 100)]   # '&' operator is used to filter the data 


# In[9]:


#Create a new “df_modified” dataframe that contains all the columns from df except for “Maxpulse”.

df_modified = df[['Duration', 'Pulse', 'Calories']].copy()  #copy method to create an another data frome with specified columns from the original dataframe.
df_modified


# In[10]:


# Delete the “Maxpulse” column from the main df dataframe

df.pop('Maxpulse')   #pop method to remove a column from the data frame
df


# In[11]:


df.dtypes


# In[12]:


#Convert the datatype of Calories column to int datatype.

df['Calories'] = df['Calories'].astype(int)  #astype function converts one data type into another
df.dtypes

