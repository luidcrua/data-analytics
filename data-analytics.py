
# Import necessary libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import datetime

# Step 1: Load the dataset (replace 'customer_data.csv' with your actual dataset path)
df = pd.read_csv('sample_customer_data.csv')

# Step 2: Initial data exploration
# Check the first few rows and data types
print(df.head())
print(df.info())

# Step 3: Handle Missing Values
# Fill missing values for 'Purchases' with 0
df['Purchases'].fillna(0, inplace=True)

# Step 4: Handle Outliers
# Cap extreme ages (greater than 100) at 100
df['Age'] = df['Age'].apply(lambda x: x if x <= 100 else 100)

# Step 5: Correct Data Types
# Convert 'LastPurchaseDate' to datetime format
df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], format='%Y-%m-%d')

# Step 6: Create New Features
# Create a new feature for days since last purchase
df['DaysSinceLastPurchase'] = (datetime.datetime.now() - df['LastPurchaseDate']).dt.days

# Step 7: Summary Statistics and Visualizations
# Display summary statistics
print(df.describe())

# Plot Age distribution
sns.histplot(df['Age'], kde=True)
plt.title('Age Distribution of Customers')
plt.show()

# Step 8: Final output
# Display cleaned and preprocessed dataset
print(df.head())
