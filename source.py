#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Start your code here


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[ ]:
import pandas as pd
import matplotlib.pyplot as plt

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
state_data = pd.read_excel(file_url, sheet_name='Food security by State')

most_recent_data = state_data[(state_data['Year'] == '2021–2023') & (state_data['State'] != 'U.S. total')]

states = most_recent_data['State']
food_insecurity = most_recent_data['Food insecurity prevalence']

plt.figure(figsize=(14, 8))
plt.bar(states, food_insecurity, color='skyblue')
plt.xlabel("State")
plt.ylabel("Food Insecurity Prevalence (%)")
plt.title("Food Insecurity Prevalence by State (2021–2023)")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


# This organizes food insecurity by state so we can see which states suffer the most and appropriately reroute potential 
# food waste to areas in need before it has the chance to be thrown out.

# In[]:
import pandas as pd
import matplotlib.pyplot as plt

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'

data = pd.read_excel(file_url, sheet_name='Food security, all households')

data_2023 = data[data['Year'] == 2023]
race_ethnicity = data_2023['Race/Ethnicity']
food_insecurity = data_2023['Food insecurity prevalence']

plt.figure(figsize=(10, 6))
plt.bar(race_ethnicity, food_insecurity, color='salmon')
plt.xlabel("Race/Ethnicity")
plt.ylabel("Food Insecurity Prevalence (%)")
plt.title("Food Insecurity by Race and Ethnicity (2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python python-exercises.ipynb')


# %%
