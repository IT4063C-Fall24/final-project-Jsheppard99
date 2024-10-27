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

desired_category = 'Race/ethnicity of households'

data_2023 = data[(data['Year'] == 2023) & (data['Category'] == desired_category)]

race_ethnicity = data_2023['Subcategory'].dropna()
food_insecurity = data_2023['Food insecure-percent'].dropna()

data_clean = pd.DataFrame({'Race/Ethnicity': race_ethnicity, 'Food Insecurity': food_insecurity}).dropna()

plt.figure(figsize=(10, 6))
plt.bar(data_clean['Race/Ethnicity'], data_clean['Food Insecurity'], color='skyblue')
plt.xlabel("Race/Ethnicity")
plt.ylabel("Food Insecurity Prevalence (%)")
plt.title("Food Insecurity by Race and Ethnicity (2023)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Through this graph we can identify which races are most affected by food insecurity and allocate more resources to those communities.

# In[]:
import pandas as pd
import matplotlib.pyplot as plt

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data = pd.read_excel(file_url, sheet_name='Food security, all households')

desired_category = 'Area of residence'

data_2023 = data[(data['Year'] == 2023) & (data['Category'] == desired_category)]

area_of_residence = data_2023['Subcategory'].dropna()
food_insecurity = data_2023['Food insecure-percent'].dropna()

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


# In[]:
import pandas as pd
import matplotlib.pyplot as plt

file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data = pd.read_excel(file_url, sheet_name='Educ, emp, disability')

filtered_data = data[['Category', 'Subcategory', 'Food insecure-1,000']]

grouped_data = filtered_data.groupby(['Category', 'Subcategory']).sum().reset_index()

plt.figure(figsize=(12, 6))
plt.bar(grouped_data['Subcategory'], grouped_data['Food insecure-1,000'], color='skyblue')
plt.xticks(rotation=90)
plt.xlabel('Subcategory')
plt.ylabel('Food Insecure (1,000)')
plt.title('Food Insecure Households by Subcategory (2023)')
plt.tight_layout()

plt.show()

# We can use this bar graph to see whether employment and 
# education status is a factor in those struggling with food insecurity, then reroute food to areas with a high concentration of these social groups.

# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python python-exercises.ipynb')


# %%
