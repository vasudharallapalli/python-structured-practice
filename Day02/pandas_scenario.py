import pandas as pd
from tabulate import tabulate  # Import tabulate for pretty printing DataFrames


df = pd.read_csv('Day02\employee_data.csv')

employee_count =  (
    df.groupby(['department'])['emp_id']
    .nunique() 
    .reset_index(name='count')  # Reset index and name the count column
    .sort_values(by='count', ascending=False)  # Sort by count in descending order
    )

print(tabulate(employee_count, headers='keys', tablefmt='grid', showindex=False))  # Readable output                              