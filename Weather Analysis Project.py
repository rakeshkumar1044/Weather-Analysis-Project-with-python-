#!/usr/bin/env python
# coding: utf-8

# 

# # (A Part of Big Data Analysis)
# 
# 

# # The Weather Dataset 
#   Here, the weather dataset is a time series data set with per-hour infromation about the weather conditions at a particular location .It records tempreture,dew point tempreture,relative humidity ,wind speed ,visibility,pressure and conditions. 

This data is available as CSV file we are going to analyze this data set usng the panda dataframe.


# # #   

# import the data set

# In[3]:


import pandas as pd
data=pd.read_csv(r"C:\Users\Dell\Desktop\PythonProject\Weatherdata\file.csv")


# In[4]:


data


# # How to Analyze  DataFrame

# # .head() 
# 
# it shows the first N rows in the data ( by default N =5)

# In[5]:


data.head(5)


# # .shape()
# 
# it show the total no. rows and no. columns of the dataframe
# 

# In[8]:


data.shape


# # .index 
# 
# this attributes provides the index of the dataframe

# In[11]:


data.index


# # .columns
# 
# it shows the name of each column

# In[12]:


data.columns


# # .dtype 
# 
# it shows the data-type of each columns

# In[13]:


data.dtypes


# # .unique()
# 
# in a columns , it shows all the unique values.
# It can be applied on a single columns only not on the whole dataframe
# 

# In[16]:


data.Weather.unique()


# # .nunique()
# 
# it shows the no. of unique values in each column. 
# it can be applied on a single column as well as on whole dataframe

# In[20]:


data.nunique()


# # .count
# 
# it  shows  the total no. of non- null in each column. it can be applied on a single column as well as on whole 
# dataframe.

# In[23]:


data.count()


# # .vlaues_counts
# 
# in a column, it shows all the unique values with their count.it can be applied on single column only.
# 

# In[27]:


data.Weather.value_counts()


# # .info()
# 
# Provide basic information about the dataframe
# 

# # Q) 1.  Find All the unique "wind speed " Values in the data.

# In[30]:


data["Wind Speed_km/h"].unique()   # Answer


# # Q) 2. Find the number of time when the Weather if exactly Clear 
# 

# In[31]:


data.head(2)


# In[33]:


data.Weather.value_counts()  # Answer  1326


# In[36]:


data[data["Weather"]=="Clear"]   # Answer 1326


# In[37]:


data.head()


# In[44]:


data.groupby('Weather').get_group("Clear")   # answer   1326


# # Q) 3.  Find the number of times when the "wind Speed was exactly 4 km/h"
# 

# In[49]:


data[data["Wind Speed_km/h"]==4]     #  Answer 474


# In[52]:


data.groupby("Wind Speed_km/h").get_group(4)   #   answer 474


# # Q. 4) Find out all the Null Values in the data

# In[55]:


data.isnull().sum()   # answer  there is no null vlaues


# In[60]:


data.notnull().sum()  # Answer No Null


# # Q  5)  Rename the Column Name "Weather" of the dataframe to "weather Condition"

# In[69]:


data.rename(columns={"Weather":"Weather Condition"},inplace=True)   # answer 


# In[70]:


data


# # Q. 6) What is the Mean "visibility"?
#     

# In[73]:


data.Visibility_km.mean()   # Answer 27.664446721311478


# In[74]:


data["Visibility_km"].mean()  # answer    27.664446721311478 


# In[77]:


data.describe()   #answer 


# # Q. 7)  What is the Standard Deviation of Pressure in this data?
# 

# In[78]:


data.head()


# In[80]:


data.Press_kPa.std()     # answer 0.8440047459486474 


# In[82]:


data["Press_kPa"].std()   # answer 0.8440047459486474 


# In[84]:


data.describe()     # answer 0.8440047459486474 


# # Q. 8) what is the Variance of "Relative Huminity" in this data?
# 

# In[87]:


data["Rel Hum_%"].var()    # Answer  286.2485501984998


# # Q.  9) Find all instances when 'Snow' was recorded.
# 

# In[89]:


data["Weather Condition"].value_counts()   # answer  390


# In[93]:


data[data["Weather Condition"]=="Snow"]   #answer 390


# In[95]:


data.groupby("Weather Condition").get_group('Snow')        #answer 390 


# In[103]:


# str.contains
data[data["Weather Condition"].str.contains("Snow")]  # Answer 583 include snow with Snow Showers,Snow,Blowing Snow,Freezing Drizzle,Snow


# # Q. 10) Find all instances when 'Wind speed is above 24' and Visibilty is 25 

# In[110]:


data[(data["Wind Speed_km/h"]>24) & (data["Visibility_km"]==25)]    #answer 308


# # Q. 11)  What is the Mean value of each column against each 'Weather Condion'

# In[131]:


data.groupby("Weather Condition").mean(numeric_only=True)     #Answer


# In[129]:


data.groupby("Weather Condition").describe()   # answer 


# # Q. 12) What is the Minimum & Maximum values of each column against each "Weather Condition"
# 

# In[133]:


data.groupby("Weather Condition").min()    #   Minimum Values


# In[135]:


data.groupby("Weather Condition").max()    # Maximum  


# # Q. 13) Show all the Record where Weather Condition is Fog.
# 

# In[137]:


data[data["Weather Condition"]=="Fog"]   # answer 150


# In[139]:


data.groupby("Weather Condition").get_group("Fog")  # Answer 150


# # Q. 14) Find all instances when "Weather is Clear " or "Visibility is above 40 ".

# In[140]:


data.head()


# In[144]:


data[(data['Weather Condition']=="Clear") | (data["Visibility_km"]>40)]    # answer 3027 rows


# # Q. 15 ) Find All instances When :
# 
# A. "Weather is clear " and "Relative Humidity is greater than 15"
# 
# or 
# 
# B.  "Visibility is above 40"

# In[152]:


data[((data["Weather Condition"]=="Clear") & (data["Rel Hum_%"]>50)) | (data["Visibility_km"]>40)]

# answer   2921


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




