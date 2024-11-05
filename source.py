#!/usr/bin/env python
# coding: utf-8

# # {Project Title}📝
# 
# ![Banner](./assets/banner.jpeg)

# ## Topic
# *What problem are you (or your stakeholder) trying to address?*
# 📝 <!-- Answer Below -->

# ## Project Question
# *What specific question are you seeking to answer with this project?*
# *This is not the same as the questions you ask to limit the scope of the project.*
# 📝 <!-- Answer Below -->

# ## What would an answer look like?
# *What is your hypothesized answer to your question?*
# 📝 <!-- Answer Below -->

# ## Data Sources
# *What 3 data sources have you identified for this project?*
# *How are you going to relate these datasets?*
# 📝 <!-- Answer Below -->

# ## Approach and Analysis
# *What is your approach to answering your project question?*
# *How will you use the identified data to answer your project question?*
# 📝 <!-- Start Discussing the project here; you can add as many code cells as you need -->

# In[ ]:


# Start your code here
import pandas as pd
import matplotlib.pyplot as plt

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data = pd.read_excel(file_url, sheet_name='Food security, all households')

# Define the desired category for filtering
desired_category = 'Race/ethnicity of households'

# Filter the data to include only rows for the year 2023 and the desired category
data_2023 = data[(data['Year'] == 2023) & (data['Category'] == desired_category)]

# Clean the race/ethnicity data by removing rows with missing values
race_ethnicity = data_2023['Subcategory'].dropna()

# Clean the food insecurity data by removing rows with missing values
food_insecurity = data_2023['Food insecure-percent'].dropna()

# Create a new DataFrame `data_clean` by combining the cleaned race/ethnicity and food insecurity data
data_clean = pd.DataFrame({'Race/Ethnicity': race_ethnicity, 'Food Insecurity': food_insecurity}).dropna()

# Create a plot to visualize the food insecurity by race/ethnicity
plt.figure(figsize=(10, 6))

plt.bar(data_clean['Race/Ethnicity'], data_clean['Food Insecurity'], color='skyblue')
plt.xlabel("Race/Ethnicity")  
plt.ylabel("Food Insecurity Prevalence (%)")  
plt.title("Food Insecurity by Race and Ethnicity (2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Through this graph we can identify which races are most affected by food insecurity and allocate more resources to those communities.


# In[5]:


file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data = pd.read_excel(file_url, sheet_name='Food security, all households')

# Define the desired category to filter by
desired_category = 'Area of residence'

# Filter the data for the year 2023 and the selected category ('Area of residence')
data_2023 = data[(data['Year'] == 2023) & (data['Category'] == desired_category)]

# Clean the 'Subcategory' column (which contains area of residence information)
area_of_residence = data_2023['Subcategory'].dropna()

# Clean the 'Food insecure-percent' column
food_insecurity = data_2023['Food insecure-percent'].dropna()

# Create a new DataFrame with the cleaned data
data_clean = pd.DataFrame({'Area of Residence': area_of_residence, 'Food Insecurity': food_insecurity}).dropna()

plt.figure(figsize=(10, 6))
plt.bar(data_clean['Area of Residence'], data_clean['Food Insecurity'], color='skyblue')
plt.xlabel("Area of Residence")
plt.ylabel("Food Insecurity Prevalence (%)")
plt.title("Food Insecurity by Area of Residence (2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# We can use this graph to compare inner city food insecurities to those who live 
# outside the downtown districts to decide whether residence in relation to the city is a factor in food scarcity.

# In[7]:


file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data = pd.read_excel(file_url, sheet_name='Educ, emp, disability')

# Make an explicit copy to avoid SettingWithCopyWarning
filtered_data = data[data['Year'] == 2023][['Subcategory', 'Sub-subcategory', 'Food insecure-percent']].copy()

# Filter by 'Sub-subcategory' for Employment
filtered_data = filtered_data[filtered_data['Sub-subcategory'].isin(['Full-time', 'Retired', 'Part-time economic reasons', 'Part-time non-economic reasons', 'Unemployed', 'Disabled'])]

# Handle missing values - Drop rows with NaN values in the relevant columns
filtered_data.dropna(subset=['Subcategory', 'Sub-subcategory', 'Food insecure-percent'], inplace=True)

# Convert 'Food insecure-percent' to numeric values (in case it's stored as strings)
filtered_data['Food insecure-percent'] = pd.to_numeric(filtered_data['Food insecure-percent'], errors='coerce')

# Drop any remaining rows with NaN values in 'Food insecure-percent' after conversion
filtered_data.dropna(subset=['Food insecure-percent'], inplace=True)

# Group data by 'Subcategory' and 'Sub-subcategory', and aggregate by summing the 'Food insecure-percent' column
grouped_data = filtered_data.groupby(['Subcategory', 'Sub-subcategory'])['Food insecure-percent'].sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(grouped_data['Sub-subcategory'], grouped_data['Food insecure-percent'], color='skyblue')
plt.xticks(rotation=45)
plt.xlabel('Sub-subcategory')
plt.ylabel('Food Insecure Percent')
plt.title('Food Insecure Households by Percent (2023)')
plt.tight_layout()

plt.show()

# We can use this bar graph to see whether employment status 
# is a factor in those struggling with food insecurity, then reroute food to areas with a high concentration of these social groups, such as retirement communities.


# In[ ]:

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
state_data = pd.read_excel(file_url, sheet_name='Food security by State')

# Filter for the most recent year range "2021–2023" and exclude the "U.S. total"
most_recent_data = state_data[(state_data['Year'] == '2021–2023') & (state_data['State'] != 'U.S. total')]

# Replace missing or null values with a placeholder, e.g., 'Unknown'
state_data['State'].fillna('Unknown', inplace=True)

# Extract data for plotting
states = most_recent_data['State']
food_insecurity = most_recent_data['Food insecurity prevalence']

# Plotting the bar graph
plt.figure(figsize=(14, 8))
plt.bar(states, food_insecurity, color='skyblue')
plt.xlabel("State")
plt.ylabel("Food Insecurity Prevalence (%)")
plt.title("Food Insecurity Prevalence by State (2021–2023)")
plt.tight_layout()
plt.show()

# This organizes food insecurity by state so we can see which states suffer the most and appropriately reroute potential 
# food waste to areas in need before it has the chance to be thrown out.

# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

