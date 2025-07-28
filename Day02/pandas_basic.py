import pandas as pd
from tabulate import tabulate  # Import tabulate for pretty printing DataFrames


df = pd.read_csv('Day02\employee_data.csv')

top_n = int(input("Enter how many top-paid employees to display: "))

Top_paid_employees = (
    df.groupby(['emp_id','name'])['salary']
    .sum()                                
    .reset_index()                        
    .sort_values(by='salary', ascending=False)
    #.head(5)  # Get top 5 highest paid employees
    .nlargest(top_n, 'salary')  # Top 5 by salary, nlargest() can be slightly faster for large datasets
    .rename(columns={'salary': 'total_salary'}) 
)
# print("Top paid employees:", Top_paid_employees.to_string(index=False))
print(tabulate(Top_paid_employees, headers='keys', tablefmt='grid')) #readable output

