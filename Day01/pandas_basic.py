import pandas as pd

# Load data from a CSV file
df = pd.read_csv('C:\\Users\\vasud\\Documents\\python-structured-practice\\Day01\\day01_sampledataset_1.csv')

# Display all employees with a salary greater than 50000
print("Employees with salary greater than 50000:")
filtered_df = df[df['salary'] > 50000]
print(filtered_df)