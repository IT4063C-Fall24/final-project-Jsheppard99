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
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# In[ ]:
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

# In[ ]:
# Splitting the Data
file_url = 'https://github.com/IT4063C-Fall24/final-project-Jsheppard99/raw/main/assets/foodsecurity_datafile.xlsx'
data1 = pd.read_excel(file_url, sheet_name='Food security, all households')
data2 = pd.read_excel(file_url, sheet_name='Educ, emp, disability')
data3 = pd.read_excel(file_url, sheet_name='Food security by State')

desired_category_area = 'Area of residence'
desired_category_race = 'Race/ethnicity of households'


race_data_filtered = data1[(data1['Year'] == 2023) & (data1['Category'] == desired_category_race)]
state_data_filtered = data3[data3['Year'] == '2021–2023']
educ_emp_data_filtered = data2[data2['Year'] == 2023][['Subcategory', 'Sub-subcategory', 'Food insecure-percent']].copy()
educ_emp_data_filtered = educ_emp_data_filtered[educ_emp_data_filtered['Sub-subcategory'].isin(['Full-time', 'Retired', 'Part-time economic reasons', 'Part-time non-economic reasons', 'Unemployed', 'Disabled'])]
area_data_filtered = data1[(data1['Year'] == 2023) & (data1['Category'] == desired_category_area)]

race_train, race_test = train_test_split(race_data_filtered, test_size=0.2, random_state=42)

area_train, area_test = train_test_split(area_data_filtered, test_size=0.2, random_state=42)

educ_emp_train, educ_emp_test = train_test_split(educ_emp_data_filtered, test_size=0.2, random_state=42)

state_train, state_test = train_test_split(state_data_filtered, test_size=0.2, random_state=42)

# In[ ]:
# Data Cleaning / Pipeline

def create_pipeline(X):
    # Ensure all categorical columns are of type 'str'
    categorical_features = X.select_dtypes(include=['object']).columns
    for col in categorical_features:
        X[col] = X[col].astype(str)  # Convert all categorical columns to strings
    
    # Separate features into categorical and numeric
    numeric_features = X.select_dtypes(include=['float64', 'int64']).columns
    categorical_features = X.select_dtypes(include=['object']).columns

    # Define transformers for numeric and categorical data
    pipeline = ColumnTransformer(
        transformers=[
            ('num', Pipeline([
                ('imputer', SimpleImputer(strategy='mean')),  # Impute missing numeric values
                ('scaler', StandardScaler())  # Standardize numeric data
            ]), numeric_features),
            ('cat', Pipeline([
                ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),  # Impute missing categorical values
                ('encoder', OneHotEncoder(handle_unknown='ignore'))  # OneHotEncode categorical data
            ]), categorical_features)
        ])

    return pipeline

# Apply pipeline to each dataset

# State data
X_state = state_train.drop(columns=['Food insecurity prevalence'])
y_state = state_train['Food insecurity prevalence']
state_pipeline = create_pipeline(X_state)
X_state_transformed = state_pipeline.fit_transform(X_state)

# Educ, emp, disability data
X_educ_emp = educ_emp_train.drop(columns=['Food insecure-percent'])
y_educ_emp = educ_emp_train['Food insecure-percent']
educ_emp_pipeline = create_pipeline(X_educ_emp)
X_educ_emp_transformed = educ_emp_pipeline.fit_transform(X_educ_emp)

# Area of residence data
X_area = area_train.drop(columns=['Food insecure-percent'])
y_area = area_train['Food insecure-percent']
area_pipeline = create_pipeline(X_area)
X_area_transformed = area_pipeline.fit_transform(X_area)

# Race/ethnicity data
X_race = race_train.drop(columns=['Food insecure-percent'])
y_race = race_train['Food insecure-percent']
race_pipeline = create_pipeline(X_race)
X_race_transformed = race_pipeline.fit_transform(X_race)

# Train-test splits with transformed data
X_state_train, X_state_test, y_state_train, y_state_test = train_test_split(X_state_transformed, y_state, test_size=0.2, random_state=42)
X_educ_emp_train, X_educ_emp_test, y_educ_emp_train, y_educ_emp_test = train_test_split(X_educ_emp_transformed, y_educ_emp, test_size=0.2, random_state=42)
X_area_train, X_area_test, y_area_train, y_area_test = train_test_split(X_area_transformed, y_area, test_size=0.2, random_state=42)
X_race_train, X_race_test, y_race_train, y_race_test = train_test_split(X_race_transformed, y_race, test_size=0.2, random_state=42)

# Output the shapes of the transformed train-test splits
print('State Train', X_state_train.shape)
print('State Test',X_state_test.shape)
print('Educ, emp, disability Train', X_educ_emp_train.shape)
print('Educ, emp, disability Test',X_educ_emp_test.shape)
print('Area Train', X_area_train.shape)
print('Area test', X_area_test.shape)
print('Race Train', X_race_train.shape)
print('Race Test',X_race_test.shape)   

# In[ ]:
# Linear Model
model = LinearRegression()  # Instantiate the Linear Regression model

# Fit the model on the training data (X_state_train, y_state_train)
model.fit(X_state_train, y_state_train)

# Predict the target variable (food insecurity level) on the test set
y_state_pred = model.predict(X_state_test)

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_state_test, y_state_pred))

# Print out the RMSE to understand how well the model performed
print(rmse)

# In[ ]:
#Classification Model
threshold = 10  # 10% threshold for food insecurity

# Create a binary target variable (high vs low food insecurity)
y_state_train_binary = (y_state_train > threshold).astype(int)
y_state_test_binary = (y_state_test > threshold).astype(int)

# Train a Decision Tree Classifier with the binary target variable
decision_tree = DecisionTreeClassifier(random_state=42)
decision_tree.fit(X_state_train, y_state_train_binary)

# Predict on the test set
y_state_pred_binary = decision_tree.predict(X_state_test)

# Calculate accuracy or other metrics
accuracy = accuracy_score(y_state_test_binary, y_state_pred_binary)
print(accuracy)


# ## Resources and References
# *What resources and references have you used for this project?*
# 📝 <!-- Answer Below -->

# In[2]:


# ⚠️ Make sure you run this cell at the end of your notebook before every submission!
get_ipython().system('jupyter nbconvert --to python source.ipynb')

