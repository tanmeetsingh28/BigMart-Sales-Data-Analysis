#!/usr/bin/env python
# coding: utf-8

# In[60]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import statistics as sts


# In[142]:


data = pd.read_csv("E:\\big mart\\bigmart_data.csv")


# In[143]:


data


# In[144]:


data.isnull().sum()


# In[145]:


data['Item_Weight'].fillna(data["Item_Weight"].mean(),inplace=True)


# In[146]:


data.isnull().sum()


# In[147]:


data['Outlet_Size'].value_counts()


# In[148]:


data['Outlet_Size'].value_counts()


# In[149]:


data['Outlet_Size'].fillna(data['Outlet_Size'].mode()[0],inplace =True)


# In[150]:


data.isnull().sum()


# In[151]:


#  How many unique products are there in the dataset?

data['Item_Identifier'].unique()


# In[152]:


#  How many unique products are there in the dataset?       #1559 unique Id

data['Item_Identifier'].nunique()     


# In[153]:


#What is the total sales revenue generated by the company?   #1,85,91,125.41 ("ONE Crore Eighty five lakh ninety thousand")
(round(data['Item_Outlet_Sales'].sum(),2))       


# In[154]:


#What is the average price of the products sold?   #140.99   ("one Fourty Rupees")

round(data['Item_MRP'].mean(),2)


# In[155]:


#What is the most commonly sold product category?     #Fruits and Vegetables 

data['Item_Type'].value_counts()


# In[156]:


plt.figure(figsize=(16, 8))

# Create the count plot
sns.countplot(data=data, x="Item_Type")

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Show the plot
plt.show()


# In[157]:


# Dictionary mapping each category to its corresponding group
category_groups = {
    'Dairy': 'Essentials',
    'Soft Drinks': 'Drinks',
    'Meat': 'Non-Vegetarian',
    'Fruits and Vegetables': 'Essentials',
    'Household': 'Essentials',
    'Baking Goods': 'Essentials',
    'Snack Foods': 'Essentials',
    'Frozen Foods': 'Essentials',
    'Breakfast': 'Essentials',
    'Health and Hygiene': 'Essentials',
    'Hard Drinks': 'Drinks',
    'Canned': 'Essentials',
    'Breads': 'Essentials',
    'Starchy Foods': 'Essentials',
    'Others': 'Others',
    'Seafood': 'Non-Vegetarian'
}



# In[158]:


data["Category_group"] = data["Item_Type"].map(category_groups)


# In[159]:


data


# In[160]:


#Which outlet type has the highest total sales revenue?    #Supermarket Type1 
data['Outlet_Type'].value_counts()


# In[161]:


Outlet_revenue = round(data.groupby('Outlet_Type')['Item_Outlet_Sales'].sum(),2).sort_values(ascending = False)
Outlet_revenue


# In[162]:


import matplotlib.pyplot as plt


Outlet_revenue = data.groupby('Outlet_Type')['Item_Outlet_Sales'].sum().round(2).sort_values(ascending=False)


plt.figure(figsize=(10, 6))
Outlet_revenue.plot(kind='bar', color='skyblue')
plt.title('Total Sales Revenue by Outlet Type')
plt.xlabel('Outlet Type')
plt.ylabel('Total Sales Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[163]:


#What is the total quantity sold for each product category?  

# First I calculate with Item_weight      #######  Fruits and Vegetables    16214.72  #######

# Then I caclculate the Product Count     #######   Fruits and Vegetables    1232 Count #######


# In[164]:


round(data.groupby("Item_Type")['Item_Weight'].sum(),2).sort_values(ascending = False)


# In[165]:


#What is the average quantity sold for each product category?
round(data.groupby("Item_Type")['Item_Weight'].mean(),2).sort_values(ascending = False)


# In[166]:


#How many unique outlets are there in the dataset?    10 Unique Outlets
data['Outlet_Identifier'].nunique()


# In[170]:


#What is the average sales revenue per outlet?  
round(data.groupby("Outlet_Identifier")["Item_Outlet_Sales"].mean(),2).sort_values(ascending = False)


# In[172]:


#In which year was the highest total sales revenue generated?  #1985 year Generated The Highest Year
round(data.groupby("Outlet_Establishment_Year")["Item_Outlet_Sales"].sum(),2).sort_values(ascending = False)


# In[175]:


# What is the average weight of the products?
data.head(1)
round(data['Item_Weight'].mean(),2)


# In[177]:


#What is the total sales revenue generated by each outlet?  
round(data.groupby("Outlet_Identifier")["Item_Outlet_Sales"].sum(),2).sort_values(ascending = False)


# In[178]:


#What is the average price of the products in each outlet type?
round(data.groupby("Outlet_Identifier")["Item_MRP"].mean(),2).sort_values(ascending = False)


# In[181]:


#What is the total quantity sold for each outlet type?
round(data.groupby("Outlet_Identifier")["Item_Weight"].sum(),2).sort_values(ascending = False)

#if we will take another approach rather than weight



# In[182]:


data['Outlet_Identifier'].value_counts()


# In[185]:


#What is the average visibility of products in each outlet size category?
round(data.groupby("Outlet_Type")["Item_Visibility"].mean(),2).sort_values(ascending = False)


# In[186]:


#What is the total sales revenue generated in each outlet location type?
round(data.groupby("Outlet_Location_Type")["Item_Outlet_Sales"].sum(),2).sort_values(ascending = False)


# In[187]:


#What is the average price of products in each product type category?
round(data.groupby("Item_Type")["Item_Outlet_Sales"].mean(),2).sort_values(ascending = False)


# In[189]:


#What is the total quantity sold for each product type category?  #In Weights
                                                                  #Product_counts
    
round(data.groupby("Item_Type")["Item_Weight"].sum(),2).sort_values(ascending = False)


# In[191]:


#products count sold
data['Item_Type'].value_counts()


# In[211]:


avg = round(data.groupby(['Outlet_Identifier', 'Outlet_Establishment_Year'])["Item_Outlet_Sales"].sum(),2)


# In[196]:


#Which outlet has the highest average sales revenue per year?
round(data.groupby("Outlet_Identifier")["Item_Outlet_Sales"].mean(),2).sort_values(ascending = False)


# In[212]:


#Done with all the 20 Questions#

