import pandas as pd

# Assuming DataFrame df has data from CSV file data.csv
df = pd.read_csv('data.csv')

# Get first 50 records
first_50_records = df.head(50)

# Calculate the mean values
mean_values = first_50_records.mean()

# Print the mean values
print("Mean values of the first 50 records:")
print(mean_values)
