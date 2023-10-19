import pandas as pd

# Assuming DataFrame df has data from CSV file data.csv
df = pd.read_csv('data.csv')

# calculate basic statistics for 'salary' column
salary_stats_subset = df['salary'].describe()
salary_stats_attribute = df.salary.describe()

# Print the statistics
print("Basic Statistics for Salary Column:")
print("subset the data frame using column name: ", salary_stats_subset)
print('use the column name as an attribute: ', salary_stats_attribute)

# ***************************************** #

# use count() method to count non-null values
# in the 'salary' column
salary_count = df['salary'].count()

# Print the count
print(f"There are {salary_count} non-null values in the 'salary' column.")

# ***************************************** #
# calculate average salary
average_salary = df['salary'].mean()

# Print the average salary
print(f"The average salary is: {average_salary}")
