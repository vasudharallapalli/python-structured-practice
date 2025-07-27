
def check_number(n:int) -> str:
    if n % 2 == 0:
        if n % 3 == 0:
            print(f"{n} is an even number and divisible by 3.")
        else:
            print(f"{n} an even number but not divisible by 3.")
    else:
        if n % 3 == 0:
            print(f"{n} is an odd number but divisible by 3.")
        else:
            print(f"{n} is an odd number and not divisible by 3.")

def check_number_compact(n:int) -> str:
    even_check = "even" if n % 2 == 0 else "odd"
    #<value_if_true> if <condition> else <value_if_false>
    #This is Python’s one-line if-else statement, also called a ternary operator.
    divisible_check = "divisible by 3" if n % 3 == 0 else "not divisible by 3"
    print(f"{n} is {even_check} and {divisible_check}.")


n = int(input("Enter a number: "))
check_number(n)
check_number_compact(n)