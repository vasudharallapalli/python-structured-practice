# Take input for 3 numbers and compute the average

def average_of_three_numbers():
    # Input three numbers from the user
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    # Calculate the average
    average = (num1 + num2 + num3) / 3

    # Print the result
    print(f"The average of {num1}, {num2}, and {num3} is: {average}")

# Call the function to execute
average_of_three_numbers()
print("average_of_three_numbers function executed successfully!")