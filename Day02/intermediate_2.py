# This script reverses a string

def reverse_string_withoutfn(input_string: str) -> None:
    for _ in range(len(list_input) - 1, -1, -1):
        print(list_input[_]) 

def reverse_string(input_string: str) -> None:
    for char in reversed(list_input):  # More readable and Pythonic
        print(char)

list_input = list(input("Enter a string: "))

reverse_string_withoutfn(list_input)
print()  # Print a newline for better readability
reverse_string(list_input)