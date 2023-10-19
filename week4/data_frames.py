import pandas as pd

# Assuming you have a DataFrame named df
# If you have loaded data from a CSV file, you can use
df = pd.read_csv('data.csv')

# Get the number of records (rows)
num_records = df.shape[0]

# Print the number of records
print(f"The DataFrame has {num_records} records.")
# ***************************************** #
# Get the total number of elements
total_elements = df.size

# Print the total number of elements
print(f"The DataFrame has {total_elements} elements.")
# ***************************************** #
# Get the column names
column_names = df.columns

# Print the column names
print("Column Names:")
for column in column_names:
    print(column)
# ***************************************** #
# Get the data types of columns
column_types = df.dtypes

# Print the data types
print("Column Types:")
print(column_types)
# ***************************************** #
# Generate summary statistics for numeric columns
summary = df.describe()

# Print the summary
print("Summary for Numeric Columns:")
print(summary)
# ***************************************** #
# calculate standard deviation for numeric columns
std_deviation = df.std()

# Print the standard deviation
print("Standard Deviation for Numeric Columns")
print(std_deviation)






