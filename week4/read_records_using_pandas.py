import pandas as pd

# Assuming you have a CSV file named 'data.csv' with a header row.
df = pd.read_csv('data.csv')

# Retrieve the first 10 records
first_10_records = df.head(10)

# Retrieve the first 20 records
first_20_records = df.head(20)

# Retrieve the first 50 records
first_50_records = df.head(50)

# Retrieve the last few records
last_few_records = df.tail(5)

# ***************************************** #
# Display the first 10 records
print(first_10_records)

# Display the first 20 records
print(first_20_records)

# Display the first 50 records
print(first_50_records)

# Display the last few records
print(last_few_records)
