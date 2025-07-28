
# This script generates multiplication tables from 1 to n, where n is provided by the user.

n = int(input("Enter a number: "))

for table in range(1, n + 1):
    for _ in range(1, 11):
        print(f"{table} x {_} = {int(table) * _}")
    print()  # Print a newline for better readability
print("Multiplication tables generated successfully.")