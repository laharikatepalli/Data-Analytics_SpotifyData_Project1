import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace 'your_dataset.csv' with the actual path to your downloaded dataset file.

df = pd.read_csv('spotify-2023.csv', encoding='latin1')




# Handle missing values
df.dropna(subset=['track_name'], inplace=True)  # Remove rows with missing track names

# Handle duplicated rows
df.drop_duplicates(subset=['track_name'], inplace=True)

# Convert date column to datetime (assuming it's in 'YYYY-MM-DD' format)
df['released_date'] = pd.to_datetime(df['released_year'].astype(str) + '-' + df['released_month'].astype(str) + '-' + df['released_day'].astype(str), format='%Y-%m-%d')

# Handle categorical data (e.g., key and mode)
df['key'] = df['key'].map({0: 'C', 1: 'C#/Db', 2: 'D', 3: 'D#/Eb', 4: 'E', 5: 'F', 6: 'F#/Gb', 7: 'G', 8: 'G#/Ab', 9: 'A', 10: 'A#/Bb', 11: 'B'})
df['mode'] = df['mode'].map({0: 'minor', 1: 'major'})

# Step 4: Data Exploration and Analysis (Optional)
# Example: Create a histogram of song release years
plt.hist(df['released_year'], bins=30)
plt.xlabel('Released Year')
plt.ylabel('Frequency')
plt.title('Song Release Year Distribution')
plt.show()



# Replace 'cleaned_data.csv' with the desired file name for your cleaned data.
#df.to_csv('cleaned_data.csv', index=False)

import os

print("Current Working Directory:", os.getcwd())



# Step 6: Load Data (Load)
# The data remains in the 'df' DataFrame

# Step 7: Documentation
# Maintain documentation to describe the data and transformations.

# Step 15: Testing (Critical)
# Develop test cases to validate your ETL process. For example, check if data transformations are correct.

# Step 16: Monitoring and Logging (Critical)
# Implement logging and monitoring as needed to track the ETL pipeline's health.

# Step 17: Deployment (Optional)
# For deployment, consider scheduling your ETL process using tools like Apache Airflow.

# Step 18: Maintenance
# Regularly update and maintain your ETL pipeline as needed.

